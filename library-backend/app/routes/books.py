from flask import Blueprint, request, jsonify
from ..models.book import Book
from ..schemas.book_schema import BookSchema
from ..database import db

books_bp = Blueprint('books', __name__, url_prefix="/books")
book_schema = BookSchema()
books_schema = BookSchema(many=True)

@books_bp.route("/", methods=["GET"])
def get_books():
    books = Book.query.all()
    return books_schema.jsonify(books)

@books_bp.route("/", methods=["POST"])
def add_book():
    data = request.get_json()
    book = book_schema.load(data, session=db.session)
    db.session.add(book)
    db.session.commit()
    return book_schema.jsonify(book), 201
