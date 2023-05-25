from werkzeug.security import check_password_hash
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db = firestore.client()
users_collection = db.collection("users")

def get_user(user):
    user_document = users_collection.document(user).get()
    user_data = user_document.to_dict()
    if user_data:
        user_data["id"] = user_document.id
        return user_data

    return None

def validate_user_password(user, password):
    user = get_user(user)
    if user:
        user_password = user["password"]
        if check_password_hash(user_password, password):
            return True
    
    return False


def get_user_todo_list(user):
    todo_list = users_collection.document(user).collection('todos').get()
    return todo_list

def create_user(username, password):
    user = users_collection.document(username)
    user.set({"password":password})


def put_todo(user,todo_description):
    todos_collection = users_collection.document(user).collection('todos')
    todos_collection.add({'description': todo_description, "done":False})

def delete_todo(user,todo_id):
    todos_collection = users_collection.document(user).collection('todos')
    todos_collection.document(todo_id).delete()

def edit_todo_description(user,todo_id, description):
    todos_collection = users_collection.document(user).collection('todos')
    todo = todos_collection.document(todo_id)
    todo.update({"description":description})

def update_todo(user,todo_id,done):
    todos_collection = users_collection.document(user).collection('todos')
    todo = todos_collection.document(todo_id)
    todo.update({"done":not done})
