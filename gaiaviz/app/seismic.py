from flask import Blueprint

seismic_app = Blueprint('data_app', __name__)


@seismic_app.route('/<line_type>/<line_number>')
def get_line():
    return 'Welcome to Gaia Vision'
