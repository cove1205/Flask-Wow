from flask import Blueprint

from .views import Hello

bp = Blueprint('bp', __name__)

bp.add_url_rule('/', view_func=Hello.as_view('hello'))