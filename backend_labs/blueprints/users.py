from flask.views import MethodView
from flask_smorest import Blueprint, abort

from backend_labs.schemas import UserSchema

from backend_labs.models.user import UserModel

from backend_labs.data import db
from sqlalchemy.exc import IntegrityError

blueprint = Blueprint("users", __name__, description="Users operations")

@blueprint.route("/user")
class UsersList(MethodView):
    @blueprint.arguments(UserSchema)
    @blueprint.response(200, UserSchema)
    def post(self, user_data):
        user = UserModel(**user_data)

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="This username is already used")

        return user

    @blueprint.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

@blueprint.route("/user/<int:user_id>")
class User(MethodView):
    @blueprint.response(200, UserSchema)
    def get(self, user_id):
        return UserModel.query.get_or_404(user_id)