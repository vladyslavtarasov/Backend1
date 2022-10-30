from lab1 import app
from flask import jsonify, request
import datetime

user_id = 2
category_id = 2
note_id = 2

CATEGORIES = [
    {
        "id": 1,
        "title": "Book"
    },
    {
        "id": 2,
        "title": "Food"
    }
]

USERS = [
    {
        "id": 1,
        "name": "Vlad"
    },
    {
        "id": 2,
        "name": "Alex"
    }
]

NOTES = [
    {
        "id": 1,
        "user_id": 1,
        "category_id": 1,
        "date_of_creating": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "price": 250
    },
    {
        "id": 2,
        "user_id": 2,
        "category_id": 2,
        "date_of_creating": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "price": 300
    }
]


@app.route("/")
def default_page():
    return "Start page"


@app.route("/user", methods=["POST"])
def create_user():
    request_data = {}
    try:
        request_data["name"] = request.get_json()["name"]
        global user_id
        user_id += 1
        request_data["id"] = user_id
    except:
        return "Error!"
    USERS.append(request_data)
    return request_data


@app.route("/category", methods=["POST"])
def create_category():
    request_data = {}
    try:
        request_data["title"] = request.get_json()["title"]
        global category_id
        category_id += 1
        request_data["id"] = category_id
    except:
        return "Error!"
    CATEGORIES.append(request_data)
    return request_data


def validation(key, value, arr):
    for i in arr:
        if i[key] == value:
            return True
    return False


@app.route("/note", methods=["POST"])
def create_note():
    request_data = request.get_json()

    try:
        if not (validation("id", request.get_json()["user_id"], USERS)
                and validation("id", request.get_json()["category_id"], CATEGORIES)):
            return "Error, user or category is not found"

        global note_id
        note_id += 1
        request_data["id"] = note_id
        request_data["date_of_creating"] = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        request_data["price"] = request.get_json()["price"]
    except:
        return "Error!"

    NOTES.append(request_data)
    return request_data


@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEGORIES})


@app.route("/users")
def get_users():
    return jsonify({"users": USERS})


@app.route("/notes")
def get_notes():
    return jsonify({"notes": NOTES})


@app.route("/notes/<int:user_id>")
def get_notes_by_user(user_id):
    user_notes = []
    for element in NOTES:
        if element['user_id'] == int(user_id):
            user_notes.append(element)
    return jsonify({"user": user_id, "notes": user_notes})


@app.get("/notes/<int:user_id>/<int:category_id>")
def get_notes_by_category(user_id, category_id):
    user_notes = []
    for element in NOTES:
        if element['user_id'] == int(user_id) and element['category_id'] == int(category_id):
            user_notes.append(element)
    return jsonify({"user": user_id, "category": category_id, "notes": user_notes})