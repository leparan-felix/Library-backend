from app import create_app
from flask import Flask
from app.config import Config
from app.database import db, migrate
from app.routes.auth import auth_bp
from app.routes.book import book_bp
from app.routes.user import user_bp
from app.routes.favorites import favorites_bp

app = create_app()
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run()
