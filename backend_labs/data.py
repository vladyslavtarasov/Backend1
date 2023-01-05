import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

CATEGORIES = [
    {
        "id": 1,
        "title": "Book"
    },
    {
        "id": 2,
        "title": "Food"
    }
]

USERS = [
    {
        "id": 1,
        "name": "Vlad"
    },
    {
        "id": 2,
        "name": "Alex"
    }
]

NOTES = [
    {
        "id": 1,
        "user_id": 1,
        "category_id": 1,
        "date_of_creating": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "price": 250
    },
    {
        "id": 2,
        "user_id": 2,
        "category_id": 2,
        "date_of_creating": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "price": 300
    }
]