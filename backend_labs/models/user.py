from backend_labs.data import db

class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    note = db.relationship(
        "NoteModel",
        back_populates="user",
        lazy="dynamic",
    )

    account = db.relationship(
        "AccountModel",
        back_populates="user",
        lazy="dynamic",
    )