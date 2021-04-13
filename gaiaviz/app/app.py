from flask import Flask


def create_app():
    """ App factory function
    """

    app = Flask(__name__)

    with app.app_context():
        from gaiaviz.app.seismic import data_app

        app.register_blueprint(data_app, url_prefix='/seismic')

        @app.route('/')
        def index():
            return 'Welcome to Gaia Vision'

    return app