from models import Collection
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate
from config import app
# from marshmallow_sqlalchemy import SQLAlchemySchema

ma = Marshmallow(app)


########################### Collection ###############################

class CollectionSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Collection
        load_instance = True
        fields = ('id', 'name', 'user_id', 'item_id')
    
    name = fields.String(
        required=True,
        validate=validate.Length(min=1, max=30, error='Collection must have a name no more than 30 characters')
    )
    user_id = fields.Integer(required=True)
    
    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "collectionbyid",
                values=dict(id="<id>")),
            "collection": ma.URLFor("collections"),
        }
    )
