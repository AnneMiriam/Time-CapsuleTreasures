from models import Collection
from marshmallow import fields, validate
from config import ma


########################### Collection ###############################

class CollectionSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Collection
        load_instance = True
        fields = ('id', 'name', 'items')
    
    name = fields.String(
        required=True,
        validate=validate.Length(min=1, max=30, error='Collection must have a name no more than 30 characters')
    )

    items = fields.List(fields.Nested('ItemSchema'), many=True, dump_only=True)

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "collectionbyid",
                values=dict(id="<id>")),
            "collection": ma.URLFor("collections"),
        }
    )
