from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required

from backend_labs.schemas import CategorySchema

from backend_labs.models.category import CategoryModel

from backend_labs.data import db
from sqlalchemy.exc import IntegrityError

blueprint = Blueprint("categories", __name__, description="Categories operations")

@blueprint.route("/category")
class CategoriesList(MethodView):
    @blueprint.arguments(CategorySchema)
    @blueprint.response(200, CategorySchema)
    @jwt_required()
    def post(self, category_data):
        category = CategoryModel(**category_data)

        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(400, message="This category already exists")

        return category

    @blueprint.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.all()

@blueprint.route("/category/<int:category_id>")
class Category(MethodView):
    @blueprint.response(200, CategorySchema)
    @jwt_required()
    def get(self, category_id):
        return CategoryModel.query.get_or_404(category_id)
