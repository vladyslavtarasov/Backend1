from flask.views import MethodView
from flask import request, abort, jsonify
from flask_smorest import Blueprint

from lab1.data import CATEGORIES

blueprint = Blueprint("categories", __name__, description="Categories operations")

@blueprint.route("/category")
class CategoriesPost(MethodView):
    def post(self):
        request_data = {}
        try:
            request_data["title"] = request.get_json()["title"]
            #global category_id
            #category_id += 1

            category_id = CATEGORIES[-1]["id"] + 1
            request_data["id"] = category_id
        except:
            return "Error!"
        CATEGORIES.append(request_data)
        return request_data

@blueprint.route("/categories")
class CategoriesGet(MethodView):
    def get(self):
        return jsonify({"categories": CATEGORIES})
