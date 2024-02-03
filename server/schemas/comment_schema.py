from models import Comment
from marshmallow import fields, validate
from config import ma


############################## Comment ###############################

class CommentSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Comment
        load_instance = True
        fields = ('id', 'comment', 'item_id')
    
    comment = fields.String(
        required=True,
        validate=validate.Length(min=1, max=250, error='Comments must be no more than 250 characters')
    )
    item_id = fields.Integer(required=True)

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "commentbyid",
                values=dict(id="<id>")),
            "collection": ma.URLFor("comments"),
        }
    )