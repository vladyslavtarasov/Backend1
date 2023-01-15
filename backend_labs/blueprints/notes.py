from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required

from backend_labs.schemas import NoteSchema
from backend_labs.schemas import NoteQuerySchema

from backend_labs.models.note import NoteModel
from backend_labs.models.category import CategoryModel
from backend_labs.models.user import UserModel
from backend_labs.models.account import AccountModel

from backend_labs.data import db
from sqlalchemy.exc import IntegrityError, NoResultFound

blueprint = Blueprint("notes", __name__, description="Notes operations")

@blueprint.route("/note")
class NotesList(MethodView):
    @blueprint.arguments(NoteQuerySchema, location="query", as_kwargs=True)
    @blueprint.response(200, NoteSchema(many=True))
    @jwt_required()
    def get(self, **kwargs):
        if len(kwargs) == 0:
            return NoteModel.query.all()

        user_id = kwargs.get("user_id")
        if user_id:
            query = NoteModel.query.filter(NoteModel.user_id == user_id)

        category_id = kwargs.get("category_id")
        if category_id:
            query = query.filter(NoteModel.category_id == category_id)

        return query.all()

    @blueprint.arguments(NoteSchema)
    @blueprint.response(200, NoteSchema)
    @jwt_required()
    def post(self, note_data):
        note = NoteModel(**note_data)
        user_id = note_data.get("user_id")
        category_id = note_data.get("category_id")
        price = note_data.get("price")

        try:
            UserModel.query.filter(UserModel.id == user_id).first_or_404()
            CategoryModel.query.filter(CategoryModel.id == category_id).first_or_404()

            account = AccountModel.query.filter(AccountModel.user_id == user_id).first_or_404()

            db.session.add(note)

            account.balance -= price

            db.session.commit()
        except IntegrityError:
            abort(400, message="Error when creating a note")

        return note

@blueprint.route("/note/<int:note_id>")
class Note(MethodView):
    @blueprint.response(200, NoteSchema)
    @jwt_required()
    def get(self, note_id):
        return NoteModel.query.get_or_404(note_id)