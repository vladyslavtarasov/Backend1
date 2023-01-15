from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required

from backend_labs.schemas import AccountSchema
from backend_labs.schemas import AccountAddBalanceSchema

from backend_labs.models.account import AccountModel

from backend_labs.data import db
from sqlalchemy.exc import IntegrityError

blueprint = Blueprint("accounts", __name__, description="Accounts operations")


@blueprint.route("/account")
class AccountsList(MethodView):
    @blueprint.arguments(AccountSchema)
    @blueprint.response(200, AccountSchema)
    @jwt_required()
    def post(self, account_data):
        account = AccountModel(**account_data)

        try:
            db.session.add(account)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Error when creating an account")

        return account

    @blueprint.response(200, AccountSchema(many=True))
    def get(self):
        return AccountModel.query.all()

    @blueprint.arguments(AccountAddBalanceSchema, as_kwargs=True)
    @blueprint.response(200, AccountSchema())
    @jwt_required()
    def put(self, **kwargs):
        account_id = kwargs.get("account_id")
        balance_to_add = kwargs.get("balance_to_add")

        try:
            account = AccountModel.query.filter(AccountModel.id == account_id).first_or_404()

            account.balance += balance_to_add
            db.session.commit()
        except IntegrityError:
            abort(400, message="Error when changing balance")

        return account


@blueprint.route("/account/<int:account_id>")
class Account(MethodView):
    @blueprint.response(200, AccountSchema)
    @jwt_required()
    def get(self, account_id):
        return AccountModel.query.get_or_404(account_id)
