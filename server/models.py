# from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates


from config import *

# password encryption
import bcrypt  

######################## classes ####################################
# User
class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    first_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)  
    _password_hash = db.Column(db.String, nullable=False)

    # relationships
    collections = db.relationship("Collection", back_populates="user", cascade="all, delete-orphan")
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete-orphan')
    forums = db.relationship("Forum", back_populates="user")
    items = association_proxy("collections", "item")


    # Validation

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Password hashes are private.")  
        # return self._password_hash

    # @password_hash.setter
    def password_set(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")
        # hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())          
        # self._password_hash = hashed.decode("utf-8")

    def password_check(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode("utf-8"))
        # return bcrypt.checkpw(password.encode("utf-8"), self._password_hash.encode("utf-8"))  

    def __repr__(self):
        return f"User {self.username}"
    


# Item
class Item(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    trade_status = db.Column(db.Boolean, nullable=False)
    ebay_link = db.Column(db.String)
    decade = db.Column(db.Integer)
    image = db.Column(db.String, nullable=False)

    # Relationships
    collections = db.relationship("Collection", back_populates="user", cascade="all, delete-orphan")
    users = association_proxy("trips", "user")

    # Validation
    

    def __repr__(self):
            return f"Item {self.name}"


# Collection => many-to-many
class Collection(db.Model):
    __tablename__ = 'collections'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    # Relationships
    user = db.relationship("User", back_populates="collections")
    item = db.relationship("Item", back_populates="collections")

    # # Validation
    # @validates("user_id", "item_id")
    # def validate_ids(self, key, id):
    #     if not isinstance(id, int):
    #         raise ValueError(f"{key} must be an integer.")
    #     return id

    def __repr__(self):
        return f"Collection {self.name}, User: {self.user_id}"


# Comment => many-to-many
class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    # Relationships
    user = db.relationship("User", back_populates="comments")
    item = db.relationship("Item", back_populates="comments")

    # Validation
    

    def __repr__(self):
        return f"Comment {self.comment}, Item: {self.item_id}"


# Forum => one-to-many
class Forum(db.Model):
    __tablename__ = 'forums'
    
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Relationships
    user = db.relationship("User", back_populates="forums")

    # Validation
    

    def __repr__(self):
        return f"Forum {self.post}, User: {self.user_id}"