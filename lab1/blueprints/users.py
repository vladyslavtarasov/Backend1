from flask.views import MethodView
from flask import request, abort, jsonify
from flask_smorest import Blueprint

from lab1.data import USERS
from lab1.schemas import UserSchema

blueprint = Blueprint("users", __name__, description="Users operations")

@blueprint.route("/user")
class UsersPost(MethodView):
    @blueprint.arguments(UserSchema)
    @blueprint.response(200, UserSchema)
    def post(self, user_data):
        user_id = USERS[-1]["id"] + 1
        user_data["id"] = user_id

        USERS.append(user_data)
        return user_data

    @blueprint.response(200, UserSchema(many=True))
    def get(self):
        return jsonify({"users": USERS})