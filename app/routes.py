from flask import Blueprint, render_template
from .data import analistas_data, resumen_candidatos

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template(
        "index.html", data=analistas_data, resumen=resumen_candidatos
    )
