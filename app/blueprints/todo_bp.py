from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from ..db_connection import delete_todo, get_user_todo_list, put_todo, delete_todo, update_todo, edit_todo_description
from ..forms import AddTodoForm, ToDoOptionsForm

todo_bp = Blueprint('todo', __name__, url_prefix='/todo', template_folder="../../templates", static_folder="../../static")

@todo_bp.route("/todo_list", methods=["GET","POST"])
@login_required
def todo_list():

    username = current_user.id
    to_do_list = get_user_todo_list(username)
    
    add_todo_form = AddTodoForm()
    todo_options_form = ToDoOptionsForm()

    if add_todo_form.validate_on_submit(): # Si se hace un post desde este form y el form es valido
        put_todo(username,{"todo_id": 0 if not to_do_list else to_do_list[-1]["todo_id"]+1,
                       "description":add_todo_form.description.data,
                       "done":False})
        
        return redirect(url_for("todo.todo_list"))

    context = {
        "add_todo_form" : add_todo_form,
        "to_do_list" : to_do_list,
        "todo_options_form" : todo_options_form
    }

    return render_template("todo_list.html", **context)

@todo_bp.route("/edit_todo/<int:todo_id>", methods=["POST"])
@login_required
def edit_todo(todo_id):

    username = current_user.id

    todo_options_form = ToDoOptionsForm()

    if todo_options_form.delete.data:
        delete_todo(username,todo_id)
    elif todo_options_form.update.data:
        update_todo(username,todo_id)
    elif todo_options_form.save.data:
        description = request.form.get("description")
        edit_todo_description(username,todo_id, description)

    return redirect(url_for("todo.todo_list"))