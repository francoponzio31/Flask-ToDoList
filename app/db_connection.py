from mongoengine import connect
from .models import UserDocModel
from werkzeug.security import check_password_hash
import urllib
import base64

def connect_to_db():

    USERNAME = urllib.parse.quote_plus(base64.b64decode("cG9uemlvMzE=").decode("utf-8"))
    PASSWORD = urllib.parse.quote_plus(base64.b64decode("bjdnUXoyQEY4WHpoTWtB").decode("utf-8"))
    DB_URI = f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.iczfviz.mongodb.net/?retryWrites=true&w=majority"

    connect(db="to_do_list", host=DB_URI)
    #* Local: connect(db="to_do_list")

def get_user(user):
    user = UserDocModel.objects( __raw__ = {"user_id" : user})
    if user:
        return user.first()

    return None

def validate_existing_user(user):
    user = UserDocModel.objects( __raw__ = {"user_id" : user})
    if user:
        return True
    
    return False

def validate_user_password(user, password):
    user = UserDocModel.objects( __raw__ = {"user_id" : user})
    if user:
        user = user.first()
        if check_password_hash(user.password, password):
            return True
    
    return False

def get_user_todo_list(user):
    user = UserDocModel.objects.get( __raw__ = {"user_id" : user})
    todo_list = user.todo_list
    return todo_list

def put_todo(user,todo):
    user = UserDocModel.objects.get( __raw__ = {"user_id" : user})
    todo_list = user.todo_list
    todo_list.append(todo)
    user.save()

def delete_todo(user,todo_id):
    user = UserDocModel.objects.get( __raw__ = {"user_id" : user})
    todo_list = user.todo_list
    for todo in todo_list:
        if todo["todo_id"] == todo_id:
            todo_list.pop(todo_list.index(todo))
    user.save()

def edit_todo_description(user,todo_id, description):
    user = UserDocModel.objects.get( __raw__ = {"user_id" : user})
    todo_list = user.todo_list
    for todo in todo_list:
        if todo["todo_id"] == todo_id:
            todo["description"] = description
    user.save()

def update_todo(user,todo_id):
    user = UserDocModel.objects.get( __raw__ = {"user_id" : user})
    todo_list = user.todo_list
    for todo in todo_list:
        if todo["todo_id"] == todo_id:
            todo["done"] = not todo["done"]
    user.save()