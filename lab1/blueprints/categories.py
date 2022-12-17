from flask.views import MethodView
from flask import request, abort, jsonify
from flask_smorest import Blueprint

from lab1.data import CATEGORIES
from lab1.schemas import CategorySchema

blueprint = Blueprint("categories", __name__, description="Categories operations")

@blueprint.route("/category")
class CategoriesPost(MethodView):
    @blueprint.arguments(CategorySchema)
    def post(self, category_data):
        category_id = CATEGORIES[-1]["id"] + 1
        category_data["id"] = category_id

        CATEGORIES.append(category_data)
        return category_data

@blueprint.route("/categories")
class CategoriesGet(MethodView):
    def get(self):
        return jsonify({"categories": CATEGORIES})
