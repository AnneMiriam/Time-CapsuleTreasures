from models import Comment
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate, pre_load
from config import app
# from marshmallow_sqlalchemy import SQLAlchemySchema

ma = Marshmallow(app)


############################## Comment ###############################

class CommentSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Comment
