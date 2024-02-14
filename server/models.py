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
    user_collections = db.relationship("UserCollection", back_populates="user", cascade="all, delete-orphan")
    collections = association_proxy("user_collections", "collection")

    # Password Validation
    @hybrid_property
    def password_hash(self):
        raise AttributeError("Password hashes are private.")  
        # return self._password_hash

    @password_hash.setter
    def password_set(self, password):
        # password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        # self._password_hash = password_hash.decode("utf-8")
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())          
        self._password_hash = hashed.decode("utf-8")

    def password_check(self, password):
        # return bcrypt.check_password_hash(self._password_hash, password.encode("utf-8"))
        return bcrypt.checkpw(password.encode("utf-8"), self._password_hash.encode("utf-8"))  

    def __repr__(self):
        return f"User {self.username}"


# Collection 
class Collection(db.Model):
    __tablename__ = 'collections'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # Relationships
    user_collections = db.relationship("UserCollection", back_populates="collection", cascade="all, delete-orphan")
    users = association_proxy('user_collections', 'user')
    item_collections = db.relationship("ItemCollection", back_populates="collection", cascade="all, delete-orphan")
    items = association_proxy('item_collections', 'item')

    def __repr__(self):
        return f"Collection {self.name}"


# UserCollection => many-to-many User and Collection
class UserCollection(db.Model):
    __tablename__ = 'user_collections'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'))

    # Relationships
    user = db.relationship("User", back_populates="user_collections")
    collection = db.relationship("Collection", back_populates="user_collections")

    def __repr__(self):
        return f"UserCollection {self.user_id} {self.collection_id}"


# Item
class Item(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    decade = db.Column(db.Integer)
    image = db.Column(db.String, nullable=False)
    likes = db.Column(db.Integer)

    # Relationships
    item_collections = db.relationship("ItemCollection", back_populates="item", cascade="all, delete-orphan")
    comments = db.relationship("Comment", back_populates="item", cascade="all, delete-orphan")
    collections = association_proxy('item_collections', 'collection')

    def __repr__(self):
            return f"Item {self.name}"


# ItemCollection => many-to-many Item and Collection
class ItemCollection(db.Model):
    __tablename__ = 'item_collections'
    
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'))

    # Relationships
    item = db.relationship("Item", back_populates="item_collections")
    collection = db.relationship("Collection", back_populates="item_collections")

    def __repr__(self):
        return f"ItemCollection: {self.collection_id}"


# Comment => one-to-many
class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    # Relationships
    item = db.relationship("Item", back_populates="comments")

    def __repr__(self):
        return f"Comment {self.comment}, Item: {self.item_id}"


# # Forum => one-to-many
# class Forum(db.Model):
#     __tablename__ = 'forums'
    
#     id = db.Column(db.Integer, primary_key=True)
#     post = db.Column(db.String)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

#     # Relationships
#     user = db.relationship("User", back_populates="forums")

#     # Validation
    

#     def __repr__(self):
#         return f"Forum {self.post}, User: {self.user_id}"