from mongoengine import Document, StringField, ListField
from flask_login import UserMixin

class UserDocModel(Document):
    """
        User model for Mongo Engine documents
    """
    meta = {"collection": "users"}
    user_id = StringField(required=True, unique=True)
    password = StringField(required=True)
    todo_list = ListField()


class UserAuthModel(UserMixin):
    """
        User model for Flask Login 
    """
    def __init__(self, username, password):
        self.id = username
        self.password = password