from flask import Flask
from .routes import bp as main_bp
from .routes import load_last_updated


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)

    @app.context_processor
    def inject_last_updated():
        return {"last_updated": load_last_updated()}

    return app
