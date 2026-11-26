#!/usr/bin/env python3
"""
Audita y sincroniza ofertas/tracker.json con ofertas/dashboard_ofertas.html,
incluyendo contadores de filtros, sección Datos/Developer y autoguardado opcional.
"""
import argparse
import datetime as dt
import functools
import http.server
import json
import re
import socketserver
import sys
import threading
import unicodedata
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
TRACKER_PATH = ROOT / "ofertas" / "tracker.json"
DASHBOARD_PATH = ROOT / "ofertas" / "dashboard_ofertas.html"
POSTULACIONES_DIR = ROOT / "postulaciones"

INACTIVE_STATES = {"cerrada", "expirada", "descartada_cerrada"}
SYNC_LOCK = threading.Lock()


def _fold(text: str | None) -> str:
    norm = unicodedata.normalize("NFKD", text or "")
    return "".join(ch for ch in norm if not unicodedata.combining(ch)).lower()


def infer_macro_cat(offer: dict) -> str:
    cat = (offer.get("categoria") or "").lower()
    rol = (offer.get("rol") or "").lower()
    if any(k in cat for k in ("ia", "agent", "llm", "ai")) and "data" not in cat[:8]:
        return "IA & Agentes"
    if any(k in cat for k in ("data", "analytics", "bi", "sql", "migraci")):
        return "Data & Analytics"
    if any(k in cat for k in ("backend", "full-stack", "software", "devops", "sap")):
        return "Backend Dev"
    if any(k in rol for k in ("agent", "llm", "ia ", "ai ")):
        return "IA & Agentes"
    if any(k in rol for k in ("data", "analyst", "analytics", "bigquery", "etl")):
        return "Data & Analytics"
    return "Backend Dev"


def infer_seccion(offer: dict) -> str:
    """Clasifica cada oferta en exactamente dos secciones principales: 'datos' o 'developer'."""
    explicit = offer.get("seccion")
    if explicit in ("datos", "developer"):
        return explicit

    oid = _fold(offer.get("id"))
    cat = _fold(offer.get("categoria"))
    rol = _fold(offer.get("rol"))
    combined = f"{cat} {rol}"

    if "c# .net" in combined or "csharp" in oid or ("sap tecnico-funcional" in combined and "abap" in combined):
        return "developer"

    data_keywords = (
        "data engineer",
        "data analyst",
        "data analytics",
        "analytics engineer",
        "data scientist",
        "data science",
        "business intelligence",
        "bases de datos",
        "sap analytics cloud",
        "migracion de datos",
        "mlops",
        "ai ml engineer",
        "machine learning intern",
        "airflow",
        "context engineer",
        "quality assurance rater",
        "value engineer",
        "deployment engineer",
        "consultor/a de inteligencia artificial (llms, apache airflow",
    )
    if any(k in combined for k in data_keywords):
        return "datos"
    return "developer"


CYL_RE = re.compile(
    r"\b(castilla y leon|valladolid|boecillo|leon|san andres del rabanedo|"
    r"ponferrada|burgos|miranda de ebro|aranda de duero|salamanca|palencia|zamora|"
    r"segovia|avila|soria)\b"
)

VALLADOLID_RE = re.compile(
    r"\b(valladolid|boecillo|laguna de duero|arroyo de la encomienda|medina del campo|tordesillas)\b"
)

LEON_RE = re.compile(
    r"\b(leon|san andres del rabanedo|ponferrada|astorga|villamanin|roperuelos|la baneza)\b"
)

MADRID_RE = re.compile(
    r"\b(madrid|tres cantos|alcobendas|pozuelo|las rozas|getafe|leganes|boadilla|torrejon)\b"
)


def infer_es_cyl(offer: dict) -> bool:
    combined = _fold(f"{offer.get('ubicacion') or ''} {offer.get('modalidad') or ''}")
    return bool(CYL_RE.search(combined))


def infer_es_valladolid(offer: dict) -> bool:
    combined = _fold(f"{offer.get('ubicacion') or ''} {offer.get('modalidad') or ''}")
    return bool(VALLADOLID_RE.search(combined))


def infer_es_leon(offer: dict) -> bool:
    combined = _fold(f"{offer.get('ubicacion') or ''} {offer.get('modalidad') or ''}")
    combined = combined.replace("castilla y leon", "")
    return bool(LEON_RE.search(combined))


def is_full_remote(offer: dict) -> bool:
    mod = _fold(offer.get("modalidad"))
    ubi = _fold(offer.get("ubicacion"))
    combined = f"{mod} {ubi}"
    if any(
        k in combined
        for k in (
            "100% remoto",
            "100% teletrabajo",
            "full-remote",
            "full remote",
            "solo teletrabajo",
            "decides trabajar desde casa",
            "decidir trabajar desde casa",
            "remoto espana",
            "espana (remoto",
            "remoto / hibrido",
            "(remoto)",
        )
    ):
        return True
    if "hibrido" in mod or "presencial" in mod:
        return False
    return bool(re.search(r"\b(remoto|teletrabajo|home based)\b", combined))


def infer_es_beca(offer: dict) -> bool:
    if "es_beca" in offer and offer["es_beca"] is not None:
        return bool(offer["es_beca"])
    combined = _fold(f"{offer.get('categoria') or ''} {offer.get('rol') or ''}")
    return bool(re.search(r"\b(beca|becas|practicas|internship|intern|graduate|orbit)\b", combined))


def infer_mod_tag(offer: dict) -> str:
    if is_full_remote(offer):
        return "100% Remoto"
    mod = _fold(offer.get("modalidad"))
    ubi = _fold(offer.get("ubicacion"))
    combined = f"{mod} {ubi}"
    es_cyl = infer_es_cyl(offer)
    has_madrid = bool(MADRID_RE.search(combined))
    if es_cyl and has_madrid:
        return "Castilla y León / Madrid"
    if es_cyl:
        return "Castilla y León"
    if has_madrid:
        if "presencial" in mod and "hibrido" not in mod:
            return "Presencial / Madrid"
        return "Híbrido / Madrid"
    if "barcelona" in combined:
        return "Híbrido (Barcelona)" if "hibrido" in mod else "Presencial (Barcelona)"
    return "Otras zonas"


def to_dashboard_offer(offer: dict, existing_html_offer: dict | None = None) -> dict:
    exp_min = offer.get("exp_min_anios")
    if exp_min is None:
        exp_min = existing_html_offer.get("exp_min", 2) if existing_html_offer else 2

    match_val = offer.get("porcentaje_match_estimado")
    if match_val is None:
        match_val = existing_html_offer.get("match", 90) if existing_html_offer else 90

    macro_cat = (
        existing_html_offer.get("macro_cat")
        if existing_html_offer and existing_html_offer.get("macro_cat")
        else infer_macro_cat(offer)
    )
    es_cyl = infer_es_cyl(offer)
    es_valladolid = infer_es_valladolid(offer)
    es_leon = infer_es_leon(offer)
    combined_loc = _fold(f"{offer.get('ubicacion') or ''} {offer.get('modalidad') or ''}")
    has_madrid = bool(MADRID_RE.search(combined_loc))
    mod_tag = infer_mod_tag(offer)
    es_madrid = (mod_tag != "100% Remoto") and has_madrid
    es_beca = infer_es_beca(offer)
    es_nueva = bool(offer.get("es_nueva", False))
    seccion = infer_seccion(offer)

    return {
        "id": offer["id"],
        "empresa": offer.get("empresa", ""),
        "rol": offer.get("rol", ""),
        "categoria": offer.get("categoria", ""),
        "macro_cat": macro_cat,
        "seccion": seccion,
        "es_beca": es_beca,
        "es_nueva": es_nueva,
        "fecha_barrido": offer.get("fecha_barrido", ""),
        "es_cyl": es_cyl,
        "es_valladolid": es_valladolid,
        "es_leon": es_leon,
        "es_madrid": es_madrid,
        "modalidad": offer.get("modalidad", ""),
        "mod_tag": mod_tag,
        "ubicacion": offer.get("ubicacion", ""),
        "salario": offer.get("salario", "") or "",
        "stack": offer.get("stack_principal") or (existing_html_offer.get("stack", []) if existing_html_offer else []),
        "fecha": offer.get("fecha_publicacion") or (existing_html_offer.get("fecha", "") if existing_html_offer else ""),
        "estado": offer.get("estado", "descubierta"),
        "decision": offer.get("decision", "pendiente"),
        "match": int(match_val),
        "exp_min": int(exp_min),
        "exp_rango": offer.get("exp_rango") or (existing_html_offer.get("exp_rango", "") if existing_html_offer else ""),
        "exp_detalle": offer.get("exp_detalle") or (existing_html_offer.get("exp_detalle", "") if existing_html_offer else ""),
        "url": offer.get("url", ""),
        "notas": offer.get("notas", ""),
    }


def extract_html_offers(html_text: str) -> list[dict]:
    m = re.search(r"const OFFERS = (\[.*?\]);\s*let decisionMap", html_text, re.S)
    if not m:
        raise RuntimeError("No se encontró el bloque 'const OFFERS = [...];' en dashboard_ofertas.html")
    return json.loads(m.group(1))


def _infer_sweep_ddmm(dash_offers: list[dict]) -> str | None:
    dates = sorted(
        {
            o.get("fecha_barrido", "")
            for o in dash_offers
            if o.get("es_nueva") and re.match(r"^\d{4}-\d{2}-\d{2}$", o.get("fecha_barrido", ""))
        }
    )
    if not dates:
        return None
    latest = dates[-1]
    return f"{latest[8:10]}/{latest[5:7]}"


def update_html_counts_and_offers(html_text: str, dash_offers: list[dict]) -> str:
    # Default view shows Empleo + Becario (INCLUDE)
    default_pool = list(dash_offers)
    becas_total = sum(1 for o in dash_offers if o.get("es_beca"))
    no_beca_total = sum(1 for o in dash_offers if not o.get("es_beca"))

    total_default = len(default_pool)
    datos_count = sum(1 for o in default_pool if o.get("seccion") == "datos")
    dev_count = sum(1 for o in default_pool if o.get("seccion") == "developer")
    nuevas_count = sum(1 for o in default_pool if o.get("es_nueva"))
    cyl_count = sum(1 for o in default_pool if o.get("es_cyl"))
    valladolid_count = sum(1 for o in default_pool if o.get("es_valladolid"))
    leon_count = sum(1 for o in default_pool if o.get("es_leon"))
    madrid_count = sum(1 for o in default_pool if o.get("es_madrid"))
    remoto_count = sum(1 for o in default_pool if o.get("mod_tag") == "100% Remoto")
    exp_0 = sum(1 for o in default_pool if o["exp_min"] == 0)
    max_1 = sum(1 for o in default_pool if o["exp_min"] <= 1)
    max_2 = sum(1 for o in default_pool if o["exp_min"] <= 2)
    min_3 = sum(1 for o in default_pool if o["exp_min"] >= 3)
    kits = sum(1 for o in default_pool if o["estado"] == "preparada_para_postular")

    offers_json = (
        json.dumps(dash_offers, ensure_ascii=False, indent=2)
        .replace("</", "<\\/")
        .replace("<!--", "\\u003c!--")
    )
    html_text = re.sub(
        r"const OFFERS = \[.*?\];(?=\s*let decisionMap)",
        lambda _: f"const OFFERS = {offers_json};",
        html_text,
        count=1,
        flags=re.S,
    )

    sweep_ddmm = _infer_sweep_ddmm(dash_offers)
    if sweep_ddmm:
        html_text = re.sub(r"(NUEVAS \()\d{2}/\d{2}(\))", rf"\g<1>{sweep_ddmm}\2", html_text)
        html_text = re.sub(r"(Solo Nuevas \()\d{2}/\d{2}(\))", rf"\g<1>{sweep_ddmm}\2", html_text)

    replacements = [
        (r'(id="tab-datos"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{datos_count}\2"),
        (r'(id="tab-developer"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{dev_count}\2"),
        (r'(data-beca="INCLUDE"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{total_default}\2"),
        (r'(data-beca="EXCLUDE"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{no_beca_total}\2"),
        (r'(data-beca="ONLY"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{becas_total}\2"),
        (r'(data-loc="ALL"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{total_default}\2"),
        (r'(data-loc="100% Remoto"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{remoto_count}\2"),
        (r'(data-loc="Valladolid"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{valladolid_count}\2"),
        (r'(data-loc="León"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{leon_count}\2"),
        (r'(data-loc="Castilla y León"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{cyl_count}\2"),
        (r'(data-loc="Híbrido / Madrid"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{madrid_count}\2"),
        (r'(data-exp="ALL"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{total_default}\2"),
        (r'(data-exp="EXP_0"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{exp_0}\2"),
        (r'(data-exp="MAX_1"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{max_1}\2"),
        (r'(data-exp="MAX_2"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{max_2}\2"),
        (r'(data-exp="MIN_3"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{min_3}\2"),
        (r'(id="new-offers-chip"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{nuevas_count}\2"),
        (r'(id="kit-only-chip"[^>]*>[^<]*\()\d+(\)</button>)', rf"\g<1>{kits}\2"),
    ]
    for pattern, repl in replacements:
        html_text = re.sub(pattern, repl, html_text)

    return html_text


def apply_decisions_and_sync(applied_ids: set[str] | None = None, discarded_ids: set[str] | None = None) -> tuple[list[dict], dict]:
    with SYNC_LOCK:
        tracker = json.loads(TRACKER_PATH.read_text(encoding="utf-8"))
        html_text = DASHBOARD_PATH.read_text(encoding="utf-8")
        html_offers = extract_html_offers(html_text)
        html_map = {o["id"]: o for o in html_offers}

        if applied_ids is not None and discarded_ids is not None:
            for o in tracker["ofertas"]:
                if o["id"] in applied_ids:
                    o["decision"] = "solicitado"
                elif o["id"] in discarded_ids:
                    o["decision"] = "descartado"
                elif o.get("estado") not in INACTIVE_STATES:
                    o["decision"] = "pendiente"

        active_tracker = [o for o in tracker["ofertas"] if o.get("estado") not in INACTIVE_STATES]
        tracker["ultima_actualizacion"] = dt.date.today().isoformat()
        tracker["total_activas_verificadas"] = len(active_tracker)
        TRACKER_PATH.write_text(json.dumps(tracker, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        dash_offers = [to_dashboard_offer(o, html_map.get(o["id"])) for o in active_tracker]
        existing_order = {oid: idx for idx, oid in enumerate(html_map.keys())}
        dash_offers.sort(
            key=lambda x: (
                0 if x.get("es_nueva") else (1 if x["id"] not in existing_order else 2),
                x["exp_min"] if (x.get("es_nueva") or x["id"] not in existing_order) else 0,
                -x["match"] if (x.get("es_nueva") or x["id"] not in existing_order) else 0,
                existing_order.get(x["id"], 0),
            )
        )
        new_html = update_html_counts_and_offers(html_text, dash_offers)
        DASHBOARD_PATH.write_text(new_html, encoding="utf-8")
        return dash_offers, tracker


class _ReusableHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


def serve_dashboard(port: int, open_browser: bool) -> int:
    ofertas_dir = str((ROOT / "ofertas").resolve())

    class DashboardHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=ofertas_dir, **kwargs)

        def log_message(self, format, *args):
            return

        def _send_json(self, code: int, payload: dict):
            raw = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(raw)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(raw)

        def do_GET(self):
            if self.path == "/":
                self.path = "/dashboard_ofertas.html"
                return super().do_GET()
            if self.path == "/api/health":
                return self._send_json(200, {"ok": True, "mode": "disk-autosave"})
            return super().do_GET()

        def do_POST(self):
            if self.path != "/api/decisions":
                return self._send_json(404, {"ok": False, "error": "Not found"})
            try:
                length = int(self.headers.get("Content-Length", "0"))
                body = self.rfile.read(length).decode("utf-8")
                payload = json.loads(body) if body else {}
                applied = set(payload.get("solicitadas", []))
                discarded = set(payload.get("descartadas", []))
                dash_offers, _ = apply_decisions_and_sync(applied, discarded)
                return self._send_json(
                    200,
                    {
                        "ok": True,
                        "total": len(dash_offers),
                        "solicitadas": len(applied),
                        "descartadas": len(discarded),
                    },
                )
            except Exception as exc:
                return self._send_json(400, {"ok": False, "error": str(exc)})

    url = f"http://127.0.0.1:{port}/dashboard_ofertas.html"
    server = _ReusableHTTPServer(("127.0.0.1", port), DashboardHandler)
    print(f"[SERVE] Dashboard con autoguardado en disco activo en: {url}")
    print("[SERVE] Pulsa Ctrl+C para detener el servidor.")
    if open_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[SERVE] Servidor detenido.")
    finally:
        server.server_close()
    return 0


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Audita y sincroniza tracker.json y dashboard_ofertas.html")
    parser.add_argument("--check", action="store_true", help="Solo audita consistencia sin modificar archivos")
    parser.add_argument("--sync", action="store_true", help="Sincroniza tracker.json -> dashboard_ofertas.html")
    parser.add_argument("--import-decisions", type=str, help="Ruta a JSON con {solicitadas:[], descartadas:[]}")
    parser.add_argument("--serve", action="store_true", help="Sirve dashboard_ofertas.html en 127.0.0.1 con autoguardado en tracker.json")
    parser.add_argument("--port", type=int, default=8765, help="Puerto local para --serve (por defecto 8765)")
    parser.add_argument("--no-browser", action="store_true", help="No abrir navegador automáticamente con --serve")
    args = parser.parse_args()

    if args.serve:
        apply_decisions_and_sync()
        return serve_dashboard(args.port, open_browser=not args.no_browser)

    if not args.check and not args.sync and not args.import_decisions:
        args.check = True

    if args.import_decisions:
        payload = json.loads(Path(args.import_decisions).read_text(encoding="utf-8"))
        apply_decisions_and_sync(set(payload.get("solicitadas", [])), set(payload.get("descartadas", [])))
        print("[OK] Decisiones importadas y sincronizadas en tracker.json y dashboard_ofertas.html.")
    elif args.sync:
        dash_offers, _ = apply_decisions_and_sync()
        print(f"[OK] Sincronizadas {len(dash_offers)} ofertas activas en tracker.json y dashboard_ofertas.html.")

    if args.check:
        tracker = json.loads(TRACKER_PATH.read_text(encoding="utf-8"))
        html_text = DASHBOARD_PATH.read_text(encoding="utf-8")
        html_offers = extract_html_offers(html_text)
        html_map = {o["id"]: o for o in html_offers}
        active_tracker = [o for o in tracker["ofertas"] if o.get("estado") not in INACTIVE_STATES]
        post_dirs = sorted([d.name for d in POSTULACIONES_DIR.iterdir() if d.is_dir()]) if POSTULACIONES_DIR.exists() else []

        t_ids = {o["id"] for o in active_tracker}
        h_ids = {o["id"] for o in html_offers}
        kits = [o["id"] for o in active_tracker if o.get("estado") == "preparada_para_postular"]
        print(f"[TRACKER] Total registros: {len(tracker['ofertas'])} | Activas: {len(active_tracker)} | Kits marcados: {len(kits)}")
        print(f"[HTML]    Ofertas embebidas: {len(html_offers)}")
        print(f"[POSTUL]  Carpetas en postulaciones/: {len(post_dirs)}")
        errors = 0
        if t_ids - h_ids:
            print(f"  ! Activas en tracker pero ausentes en HTML: {sorted(t_ids - h_ids)}")
            errors += 1
        if h_ids - t_ids:
            print(f"  ! En HTML pero no activas en tracker: {sorted(h_ids - t_ids)}")
            errors += 1
        missing_match = [o["id"] for o in active_tracker if o.get("porcentaje_match_estimado") is None]
        if missing_match:
            print(f"  ! Ofertas sin porcentaje_match_estimado en tracker.json: {missing_match}")
            errors += 1
        field_drifts = []
        for o in active_tracker:
            ho = html_map.get(o["id"])
            if not ho:
                continue
            expected = to_dashboard_offer(o, ho)
            for k in ("decision", "seccion", "es_beca", "es_nueva", "es_cyl", "es_valladolid", "es_leon", "es_madrid", "mod_tag", "match", "exp_min"):
                if ho.get(k) != expected.get(k):
                    field_drifts.append(f"{o['id']}.{k}: html={ho.get(k)!r} != expected={expected.get(k)!r}")
        if field_drifts:
            print(f"  ! Desajustes de atributos entre tracker.json y HTML ({len(field_drifts)}):")
            for fd in field_drifts[:15]:
                print(f"      - {fd}")
            errors += 1
        expected_static_html = update_html_counts_and_offers(html_text, html_offers)
        if html_text != expected_static_html:
            print("  ! Desajuste en contadores estáticos o etiquetas de fecha en dashboard_ofertas.html (ejecuta --sync).")
            errors += 1
        if errors:
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
