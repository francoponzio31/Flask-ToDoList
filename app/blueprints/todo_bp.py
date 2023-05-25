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

    if add_todo_form.validate_on_submit(): 
        todo_description = add_todo_form.description.data
        put_todo(username,todo_description)
        
        return redirect(url_for("todo.todo_list"))

    context = {
        "add_todo_form" : add_todo_form,
        "to_do_list" : to_do_list,
        "todo_options_form" : todo_options_form
    }

    return render_template("todo_list.html", **context)

@todo_bp.route("/edit_todo/<todo_id>/<int:done>", methods=["POST"])
@login_required
def edit_todo(todo_id,done):

    username = current_user.id

    todo_options_form = ToDoOptionsForm()

    if todo_options_form.delete.data:
        delete_todo(username,todo_id)
    elif todo_options_form.update.data:
        update_todo(username,todo_id,done)
    elif todo_options_form.save.data:
        description = request.form.get("description")
        edit_todo_description(username,todo_id, description)

    return redirect(url_for("todo.todo_list"))