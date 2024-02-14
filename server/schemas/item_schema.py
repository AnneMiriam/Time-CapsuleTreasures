from models import Item
from marshmallow import Schema, fields, validate, pre_load
from config import ma


############################# Item ##################################

class ItemSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Item
        load_instance = True
        fields = ('id', 'name', 'image', 'description', 'category', 'decade', 'likes', 'comments', 'collection_id')

    name = fields.String(required=True,
        validate=validate.Length(min=1, max=80, error='name must be between 1 and 80 characters')
        )
    description = fields.String(required=True,
        validate=validate.Length(min=1, max=255, error='name must be between 1 and 255 characters')
        )
    category = fields.String(
        required=True,
        validate=validate.OneOf(choices=['Toys', 'VHS', 'Books', 'Stuffed Animals', 'Games', 'Clothes', 'DVD', 'Other']),
    )
    # decade = fields.Integer(
    #     required=False,
    #     validate=validate.OneOf(choices=[1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000]),
    # )
    # image = fields.String(required=True)
    
    likes = fields.Integer(default=0)
    
    comments = fields.List(fields.Nested("CommentSchema"), many=True, dump_only=True)
    
    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "itembyid",
                values=dict(id="<id>")),
            "collection": ma.URLFor("items"),
        }
    )
    
    collection_id = fields.Integer()