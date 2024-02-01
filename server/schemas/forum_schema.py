from models import Forum
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate, pre_load
from config import app
# from marshmallow_sqlalchemy import SQLAlchemySchema

ma = Marshmallow(app)


############################### Forum ################################## 

class ForumSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Forum