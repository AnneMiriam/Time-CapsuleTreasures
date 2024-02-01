from models import Collection
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate, pre_load
from config import app
# from marshmallow_sqlalchemy import SQLAlchemySchema

ma = Marshmallow(app)


########################### Collection ###############################

class CollectionSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Collection
