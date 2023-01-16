from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token
from flask import jsonify
from flask_jwt_extended import jwt_required

from backend_labs.schemas import UserSchema, UserLogin

from backend_labs.models.user import UserModel


from backend_labs.data import db
from sqlalchemy.exc import IntegrityError

blueprint = Blueprint("users", __name__, description="Users operations")

@blueprint.route("/register")
class UserRegister(MethodView):
    @blueprint.arguments(UserSchema)
    @blueprint.response(200, UserSchema)
    def post(self, user_data):
        #user = UserModel(**user_data)
        user = UserModel(name=user_data["name"],
                         password=pbkdf2_sha256.hash(user_data["password"]))

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="This username is already used")

        return jsonify({"id": user.id, "username": user.name})

@blueprint.route("/users")
class UserRegister(MethodView):
    @jwt_required()
    @blueprint.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

@blueprint.route("/login")
class UserLogin(MethodView):
    @blueprint.arguments(UserLogin)
    @blueprint.response(200, UserLogin)
    def post(self, user_data):
        user = UserModel.query.filter_by(name=user_data["username"]).first()
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id)
            return jsonify({"status": "Ok", "access_token": access_token})

        return abort(400, message="User not found")

@blueprint.route("/user/<int:user_id>")
class User(MethodView):
    @blueprint.response(200, UserSchema)
    @jwt_required()
    def get(self, user_id):
        return UserModel.query.get_or_404(user_id)