from models import Comment
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate
from config import app
# from marshmallow_sqlalchemy import SQLAlchemySchema

ma = Marshmallow(app)


############################## Comment ###############################

class CommentSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Comment
        load_instance = True
        fields = ('id', 'comment', 'user_id', 'item_id')
    
    comment = fields.String(
        required=True,
        validate=validate.Length(min=1, max=250, error='Comments must be no more than 250 characters')
    )
    user_id = fields.Integer(required=True)
    item_id = fields.Integer(required=True)
    
    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "commentbyid",
                values=dict(id="<id>")),
            "collection": ma.URLFor("comments"),
        }
    )