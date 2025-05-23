import json
from pathlib import Path
from flask import Blueprint, render_template
from .data import (
    resumen_candidatos,
    fuentes,
    candidatos_tdj,
    candidatos_boleta_azul,
    candidatos_lista_negra,
)

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
        resumen=resumen_candidatos,
        fuentes=fuentes,
    )


@bp.route("/acerca")
def acerca():
    return render_template("acerca.html")


@bp.route("/boleta-verde")
def boleta_verde():
    return render_template("boleta_verde.html", candidatos_tdj=candidatos_tdj)


@bp.route("/boleta-azul")
def boleta_azul():
    return render_template(
        "boleta_azul.html", candidatos_boleta_azul=candidatos_boleta_azul
    )


@bp.route("/lista-negra")
def lista_negra():
    return render_template(
        "lista_negra.html", candidatos_lista_negra=candidatos_lista_negra
    )
