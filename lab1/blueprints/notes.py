from flask.views import MethodView
from flask import request, abort, jsonify
from flask_smorest import Blueprint
import datetime

from lab1.data import NOTES
from lab1.data import USERS
from lab1.data import CATEGORIES

blueprint = Blueprint("notes", __name__, description="Notes operations")

@blueprint.route("/note")
class NotesPost(MethodView):
    def post(self):
        request_data = request.get_json()

        try:
            if not (validation("id", request.get_json()["user_id"], USERS)
                    and validation("id", request.get_json()["category_id"], CATEGORIES)):
                return "Error, user or category is not found"

            #global note_id
            #note_id += 1

            note_id = NOTES[-1]["id"] + 1
            request_data["id"] = note_id
            request_data["date_of_creating"] = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            request_data["price"] = request.get_json()["price"]
        except:
            return "Error!"

        NOTES.append(request_data)
        return request_data

@blueprint.route("/notes")
class NotesGet(MethodView):
    def get(self):
        return jsonify({"notes": NOTES})

@blueprint.route("/notes/<int:user_id>")
def get_notes_by_user(user_id):
    user_notes = []
    for element in NOTES:
        if element['user_id'] == int(user_id):
            user_notes.append(element)
    return jsonify({"user": user_id, "notes": user_notes})


@blueprint.route("/notes/<int:user_id>/<int:category_id>")
def get_notes_by_category(user_id, category_id):
    user_notes = []
    for element in NOTES:
        if element['user_id'] == int(user_id) and element['category_id'] == int(category_id):
            user_notes.append(element)
    return jsonify({"user": user_id, "category": category_id, "notes": user_notes})

def validation(key, value, arr):
    for i in arr:
        if i[key] == value:
            return True
    return False
