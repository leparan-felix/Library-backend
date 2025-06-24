from marshmallow_sqlalchemy import SQLAlchemyAutoSchema # type: ignore
from ..models.book import Book

class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True
