from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)

class NoteSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    price = fields.Float(required=True)

class NoteQuerySchema(Schema):
    user_id = fields.Int()
    category_id = fields.Int()

class AccountSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    balance = fields.Float(required=True)

class AccountAddBalanceSchema(Schema):
    account_id = fields.Int(required=True)
    balance_to_add = fields.Float(required=True)