from marshmallow import Schema, fields

class UserSchema(Schema):
    name = fields.Str(required=True)

class CategorySchema(Schema):
    title = fields.Str(required=True)

class NoteSchema(Schema):
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    date_of_creating = fields.DateTime("%d.%m.%Y %H:%M:%S", required=False)
    price = fields.Float(required=True)