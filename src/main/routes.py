import click
from flask import render_template, url_for

from src.main import bp


@bp.route("/")
def index():
    return render_template(
        "index.html",
        APIs=(
            ("Book", url_for("book.doc"), "📚"),
            ("User", url_for("user.doc"), "🙋‍♂️"),
        ),
    )
