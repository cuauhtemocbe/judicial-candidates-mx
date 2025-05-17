import json
from pathlib import Path
from flask import Blueprint, render_template
from .data import analistas_data, resumen_candidatos, fuentes

bp = Blueprint("main", __name__)


def load_last_updated():
    try:
        path = Path(__file__).parent / "data" / "last_updated.json"
        with open(path) as f:
            return json.load(f).get("last_updated")
    except Exception:
        return "Fecha no disponible"


@bp.route("/")
def index():
    return render_template(
        "index.html",
        data=analistas_data,
        resumen=resumen_candidatos,
        fuentes=fuentes,
    )


@bp.route("/acerca")
def acerca():
    return render_template("acerca.html")
