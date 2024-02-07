from models import User
from marshmallow import fields, validate, pre_load
from config import ma


############################ User #################################
class UserSchema(ma.SQLAlchemySchema):
# class UserSchema(ma.SQLAlchemySchema):
    class Meta():
        model = User
        load_instance = True
        fields = ('id', 'first_name', 'username', 'email', 'collections')
        
    first_name = fields.String(
        required=True, 
        validate=validate.Length(min=1, max=15, error='First name must be 1-15 characters')
    )
    username = fields.String(
        required=True,
        validate=validate.Length(min=5, max=20, error='Username must be between 5 and 20 characters')
    )
    # email = fields.Email(required=True)
    email = fields.String(required=True)
    password = fields.String(
        load_only=True, 
        required=True,
        validate=[
            validate.Length(min=8, max=16, error='Password must be between 8 and 16 characters'),
            # At least one lowercase letter
            lambda p: any(c.islower() for c in p),
            # At least one uppercase letter
            lambda p: any(c.isupper() for c in p),
            # At least one number
            lambda p: any(c.isdigit() for c in p),
        ],
    )
    collections = fields.List(fields.Nested('CollectionSchema', exclude=('items',)), many=True, dump_only=True)
    
    # @pre_load
    # def normal_input(self, data, **kwargs):
    #     # Convert email to lowercase before validation
    #     data['email'] = data.get('email', '').lower().strip()
    #     return data
    
    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "userbyid",
                values=dict(id="<id>")),
            "collection": ma.URLFor("users"),
        }
    )

