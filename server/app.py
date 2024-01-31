# Remote library imports
from flask import Flask, request, make_response, session, abort
from flask_restful import Resource
from os import environ
from dotenv import load_dotenv
from schemas import UserSchema, ItemSchema, CollectionSchema, CommentSchema, ForumSchema
# Add your model imports
from models import User, Item, Collection, Comment, Forum
from marshmallow import ValidationError

# from flask_bcrypt import Bcrypt

# Local imports
from config import app, db, api

# Secret Key
load_dotenv(".env")
app.secret_key = environ.get("SECRET_KEY")

# ma = Marshmallow(app)
# user_schema = UserSchema(session=db.session)
################### Home Page #####################
@app.route("/")
def index():
    return "<h1>Time Capsule Treasures</h1>"

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
            new_user.password_hash = request.json["password"]
            db.session.add(new_user)
            db.session.commit()
            session["user_id"] = new_user.id
            return make_response(new_user.to_dict(), 201)
        except ValueError as e:
            return make_response({"error": f"{e}"}, 400)


class Login(Resource):
    def post(self):
        try:
            username = request.json["username"]
            password = request.json["password"]

            user = User.query.filter_by(username=username).first()
            if user and user.authenticate(password):
                session["user_id"] = user.id
                return user_schema.dump(user), 200
            session.clear()
            return {"error": "Incorrect username or password"}, 401
        except Exception as e:
            return {"error": f"{e}"}, 403


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
user_schema = UserSchema(session=db.session)
users_schema = UserSchema(many=True, exclude=("items",), session=db.session)

class Users(Resource):
    def get(self):
        if "user_id" in session:
            try:
                users = users_schema.dump(User.query)
                return users, 200
            except Exception as e:
                abort(400, str(e))
        return {"message": "Not Authorized"}, 401
        # try:
        #     return make_response([user.to_dict() for user in User.query.all()], 200)
        # except Exception as e:
        #     return make_response({"Error": "Could not get data"}, 400)


class UserById(Resource):
    def get(self, id):
        user = User.query.get(id)
        if user:
            return make_response(user.to_dict(), 200)
        return make_response({"error": "User not found"}, 404)

########################## Item ##############################


class Items(Resource):
    def get(self):
        pass

    def post(self):
        pass


class ItemById(Resource):
    def patch(self,id):
        pass

    def delete(self,id):
        pass

############################ Collection ############################


class Collections(Resource):
    def get(self):
        pass

    def post(self):
        pass


class CollectionById(Resource):
    def patch(self,id):
        pass

    def delete(self,id):
        pass

############################# Comment #############################


class Comments(Resource):
    def get(self):
        pass

    def post(self):
        pass


class CommentById(Resource):
    def delete(self,id):
        pass

################################ Forum ######################################


class Forums(Resource):
    def get(self):
        pass

    def post(self):
        pass


class ForumById(Resource):
    def patch(self,id):
        pass

    def delete(self,id):
        pass


api.add_resource(Signup, "/sign_up")
api.add_resource(Login, "/login")
api.add_resource(Logout, "/logout")
api.add_resource(CheckSession, "/check_session")
api.add_resource(Users, "/users")
api.add_resource(UserById, "/users/<int:id>")
api.add_resource(Items, "/items")
api.add_resource(ItemById, "/items/<int:id>")
api.add_resource(Collections, "/collections")
api.add_resource(CollectionById, "/collections/<int:id>")
api.add_resource(Comments, "/comments")
api.add_resource(CommentById, "/comments/<int:id>")
api.add_resource(Forums, "/forums")
api.add_resource(ForumById, "/forums/<int:id>")


if __name__ == "__main__":
    app.run(port=5555, debug=True)