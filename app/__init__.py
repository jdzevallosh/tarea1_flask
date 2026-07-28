from flask import Flask
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Ruta de prueba inicial
    @app.route("/")
    def index():
        return "configurado correctamente"

    return app