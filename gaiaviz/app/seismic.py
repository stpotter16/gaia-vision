from flask import Blueprint

seismic_app = Blueprint('data_app', __name__)


@seismic_app.route('/<line_type>/<line_number>', methods=['GET'])
def get_line():
    array = ''
    return 'Welcome to Gaia Vision'
