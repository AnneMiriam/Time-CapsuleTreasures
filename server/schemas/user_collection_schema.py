from models import UserCollection
from marshmallow import Schema, fields, validate, pre_load
from config import ma


class UserCollectionSchema(ma.SQLAlchemySchema):

    class Meta():
        model = UserCollection
        load_instance = True
        fields = ("user_id", "collection_id")
