from .books import books_bp
from .auth import auth_bp

def register_routes(app):
    app.register_blueprint(books_bp)
    app.register_blueprint(auth_bp)
