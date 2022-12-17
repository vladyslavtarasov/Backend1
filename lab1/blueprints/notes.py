from flask.views import MethodView
from flask import request, abort, jsonify
from flask_smorest import Blueprint
import datetime

from lab1.data import NOTES
from lab1.data import USERS
from lab1.data import CATEGORIES
from lab1.schemas import NoteSchema

blueprint = Blueprint("notes", __name__, description="Notes operations")

@blueprint.route("/note")
class NotesPost(MethodView):
    @blueprint.arguments(NoteSchema)
    def post(self, note_data):

        if not (validation("id", note_data["user_id"], USERS)
                and validation("id", note_data["category_id"], CATEGORIES)):
            return "Error, user or category is not found"

        note_id = NOTES[-1]["id"] + 1
        note_data["id"] = note_id

        if 'date_of_creating' not in note_data:
            note_data["date_of_creating"] = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        NOTES.append(note_data)
        return note_data

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
