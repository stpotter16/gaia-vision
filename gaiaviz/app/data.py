from flask import Blueprint

data_app = Blueprint('data_app', __name__)


@data_app.route('/')
def index():
    return 'Welcome to Gaia Vision'
