from flask import Flask


def create_app():
    """ App factory function
    """

    app = Flask(__name__)

    with app.app_context():
        from gaiaviz.app.data import data_app

        app.register_blueprint(data_app, url_prefix='/data')

    return app