from marshmallow_sqlalchemy import SQLAlchemyAutoSchema # type: ignore
from ..models.favorite import Favorite

class FavoriteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Favorite
        load_instance = True
