import subprocess
from flask import Blueprint, render_template
from .data import analistas_data, resumen_candidatos, fuentes

bp = Blueprint("main", __name__)


def get_last_commit_date():
    try:
        result = subprocess.check_output(
            ["git", "log", "-1", "--format=%cd", "--date=short"],
            universal_newlines=True,
        )
        return result.strip()
    except Exception:
        return "Fecha no disponible"


@bp.route("/")
def index():
    return render_template(
        "index.html",
        data=analistas_data,
        resumen=resumen_candidatos,
        fuentes=fuentes,
        last_updated=get_last_commit_date(),
    )


@bp.route("/acerca")
def acerca():
    return render_template("acerca.html")
