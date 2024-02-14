# Remote library imports
from flask import request, make_response, session, render_template
from flask_restful import Resource
from schemas.user_schema import UserSchema  
from schemas.item_schema import ItemSchema
from schemas.collection_schema import CollectionSchema
from schemas.comment_schema import CommentSchema

# Add your model imports
from models import User, Item, Collection, Comment, UserCollection, ItemCollection
from marshmallow import ValidationError

# from flask_bcrypt import Bcrypt
## ma = Marshmallow(app)
# Local imports
from config import app, db, api


user_schema = UserSchema(session=db.session)
################### Home Page #####################
@app.route("/")
def index():
    return render_template("index.html")
    # return "<h1>Time Capsule Treasures</h1>"

# @app.errorhandler(404)
# def not_found(e):
#     return render_template("index.html")

######################Login/SignUp/CheckSession ##########################

class Signup(Resource):
    def post(self):
        try:
            new_user = User(
                username = request.json['username'],
                email = request.json['email'],  
                first_name = request.json['first_name']
            )
            user_schema.validate(new_user)
            # new_user.password_hash = request.json["password"]
            new_user.password_set(request.json["password"])
            db.session.add(new_user)
            db.session.commit()
            session["user_id"] = new_user.id
            return user_schema.dump(new_user), 201
        except ValueError as e:
            return {"error": f"{e}"}, 400


class Login(Resource):
    def post(self):
        username = request.json["username"]
        password = request.json["password"]

        user = User.query.filter_by(username=username).first()
        if user and user.password_check(password):
            session["user_id"] = user.id
            return user_schema.dump(user), 200
        # session.clear()
        return {"error": "Incorrect username or password"}, 401



class Logout(Resource):
    def delete(self):
        session.clear()
        return {}, 204


class CheckSession(Resource):
    def get(self):
        user = User.query.get(session.get("user_id"))
        if user:
            return user_schema.dump(user), 200
        else:
            return {}, 401


################################# User #################################
# user_schema = UserSchema(session=db.session)
users_schema = UserSchema(many=True, exclude=("collections",), session=db.session)

class Users(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users), 200
        # if "user_id" in session:
        #     try:
        #         users = users_schema.dump(User.query)
        #         return users, 200
        #     except Exception as e:
        #         abort(400, str(e))
        # return {"message": "Not Authorized"}, 401


class UserById(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()
        if user:
            return user_schema.dump(user), 200
        return make_response({"error": "User not found"}, 404)

######################### Collection #########################
collection_schema = CollectionSchema(session=db.session)
collections_schema = CollectionSchema(many=True, exclude=("items",), session=db.session)

class Collections(Resource):
    # Collections should be visible to all users on home page
    def get(self):
        user_id = session.get("user_id")
        if user_id:
            user = db.session.get(User, user_id)
            if user:
                collections = user.collections
                return collections_schema.dump(collections), 200
            return {"error": "User not found"}, 404
        return {"error": "Must be signed in to view collections"}, 401
        
    def post(self):
        # Collections should only be created when logged in
        user = db.session.get(User, session.get('user_id'))
        if user:
            try:
                data = request.get_json()
                collection = collection_schema.load(data)
                # Associate the collection with the current user
                user_collection = UserCollection(user=user, collection=collection)
                db.session.add(user_collection)
                db.session.commit()
                return collection_schema.dump(collection), 201
            except ValidationError:
                return {'error': 'Bad request'}, 400
        return {'error': 'User must be logged in'}, 401



class CollectionById(Resource):
    def get(self, id):
        collection = db.session.get(Collection, id)
        if collection:
            return collection_schema.dump(collection), 200
        return make_response({"error": "Collection not found"}, 404)


    def delete(self,id):
        collection = db.session.get(Collection, id)
        if not collection:
            return {'error': 'Collection not found'}, 404
        else:
            db.session.delete(collection)
            db.session.commit()
            return {'message': 'Collection deleted successfully'}, 204


########################## Item ##############################
item_schema = ItemSchema(session=db.session)
items_schema = ItemSchema(many=True, exclude=('comments',), session=db.session)

class Items(Resource):
    def get(self):
        items = Item.query.all()
        if not items:
            return {"error": "No items found."}, 404
        return items_schema.dump(items), 200

    def post(self):
        data = request.get_json()
        
        try:
            # new_item = Item(
            #     name = request.json['name'],
            #     category = request.json['category'],
            #     description = request.json['description'], 
            #     decade = request.json['decade'],
            #     image = request.json['image'],
            # )
            
            # Associate currrent collection with item
            collection =  Collection.query.get(data.get("collection_id"))
            if not collection:
                raise ValidationError
            item = item_schema.load(data)
            item_collection = ItemCollection(collection=collection, item=item)
            db.session.add(item_collection)
            db.session.commit()
            return item_schema.dump(item), 201
        except ValidationError as e:
            return {'errors': e.__str__()}, 400
            


class ItemById(Resource):
    def get(self, id):
        item = db.session.get(Item, id)
        if item:
            return item_schema.dump(item), 200
        return make_response({"error": "Item not found"}, 404)
    
    def patch(self,id):
        item = Item.query.get(id)
        if item:
            try:
                data = request.get_json()
                update_item = item_schema.load(data, instance=item, partial=True)
                db.session.commit()
                return item_schema.dump(update_item), 200
            except ValidationError as e:
                return {'error': 'Bad request'}, 400
        return {'error': 'Item not found'}, 404

    def delete(self,id):
        item = Item.query.get(id)
        if not item:
            return {'error': 'Item not found'}, 404
        else:
            db.session.delete(item)
            db.session.commit()
            return {'message': 'Item deleted successfully'}, 204


############################# Comment #############################
comment_schema = CommentSchema(session=db.session)
comments_schema = CommentSchema(many=True, session=db.session)

class Comments(Resource):
    # comments are only visible on the item that matches it's item_id
    def get(self):
        comment = Comment.query.all()
        return comments_schema.dump(comment), 200

    def post(self):
        ## only users can leave a comment
        # user = User.query.get(session.get('user_id'))
        # if user:
        #     try:
        #         data = request.get_json()
        #         comment = comment_schema.load(data)
        #         db.session.add(comment)
        #         db.session.commit()
        #         return comment_schema(comment), 201
        #     except ValidationError:
        #         return {'error': 'Bad request'}, 400
        # return {'error': 'User must be logged in'}, 401
        try:
            data = request.get_json()
            comment = comment_schema.load(data)
            db.session.add(comment)
            db.session.commit()
            return comment_schema(comment), 201
        except ValidationError:
            return {'error': 'Bad request'}, 400



class CommentById(Resource):
    def delete(self,id):
        pass


# ################################ Forum ######################################

# class Forums(Resource):
#     def get(self):
#         pass

#     def post(self):
#         pass


# class ForumById(Resource):
#     def patch(self,id):
#         pass

#     def delete(self,id):
#         pass


################################## Routes #####################################

api.add_resource(Signup, "/sign_up")
api.add_resource(Login, "/login")
api.add_resource(Logout, "/logout")
api.add_resource(CheckSession, "/check_session")
api.add_resource(Users, "/api/users")
api.add_resource(UserById, "/api/users/<int:id>")
api.add_resource(Items, "/api/items")
api.add_resource(ItemById, "/api/items/<int:id>")
api.add_resource(Collections, "/api/collections")
api.add_resource(CollectionById, "/api/collections/<int:id>")
api.add_resource(Comments, "/api/comments")
api.add_resource(CommentById, "/api/comments/<int:id>")
# api.add_resource(Forums, "/forums")
# api.add_resource(ForumById, "/forums/<int:id>")


if __name__ == "__main__":
    app.run(port=5555, debug=True)