from flask import Flask
from config.config import Config
from app.routes import auth, dashboard, infra

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Registrar rutas
    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(infra.bp)

    return app
