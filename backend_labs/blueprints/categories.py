from flask.views import MethodView
from flask import request, abort, jsonify
from flask_smorest import Blueprint

from backend_labs.data import CATEGORIES
from backend_labs.schemas import CategorySchema

blueprint = Blueprint("categories", __name__, description="Categories operations")

@blueprint.route("/category")
class CategoriesPost(MethodView):
    @blueprint.arguments(CategorySchema)
    @blueprint.response(200, CategorySchema)
    def post(self, category_data):
        category_id = CATEGORIES[-1]["id"] + 1
        category_data["id"] = category_id

        CATEGORIES.append(category_data)
        return category_data

    @blueprint.response(200, CategorySchema(many=True))
    def get(self):
        return jsonify({"categories": CATEGORIES})