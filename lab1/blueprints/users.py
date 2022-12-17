from flask.views import MethodView
from flask import request, abort, jsonify
from flask_smorest import Blueprint

from lab1.data import USERS

blueprint = Blueprint("users", __name__, description="Users operations")

@blueprint.route("/user")
class UsersPost(MethodView):
    def post(self):
        request_data = {}
        try:
            request_data["name"] = request.get_json()["name"]
            #global user_id
            #user_id += 1

            user_id = USERS[-1]["id"] + 1
            request_data["id"] = user_id
        except:
            return "Error!"
        USERS.append(request_data)
        return request_data

@blueprint.route("/users")
class UsersGet(MethodView):
    def get(self):
        return jsonify({"users": USERS})