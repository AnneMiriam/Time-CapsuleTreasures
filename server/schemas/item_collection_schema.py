from models import ItemCollection
from marshmallow import Schema, fields, validate, pre_load
from config import ma


class ItemCollectionSchema(ma.SQLAlchemySchema):

    class Meta():
        model = ItemCollection
        load_instance = True
        fields = ("item_id", "collection_id")
