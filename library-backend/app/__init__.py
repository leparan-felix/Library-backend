# app/__init__.py
from flask import Flask
from .config import Config
from .database import db
from flask_cors import CORS # type: ignore
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager # type: ignore
from .routes import register_routes

jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    register_routes(app)

    return app
