from marshmallow_sqlalchemy import SQLAlchemyAutoSchema # type: ignore
from ..models.user import User

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ["password"]
