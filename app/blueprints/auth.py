from flask import Blueprint, render_template, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user
from ..models import UserAuthModel
from ..forms import LogInForm, SignUpForm
from ..db_connection import create_user, get_user
from werkzeug.security import generate_password_hash


auth = Blueprint('auth', __name__, url_prefix='/auth', template_folder="../../templates", static_folder="../../static")

login_manager = LoginManager()
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user):

    user_data = get_user(user)

    return UserAuthModel(user_data["id"], user_data["password"])


@auth.route("/login", methods=["GET","POST"])
def login():

    login_form = LogInForm()

    if login_form.validate_on_submit():

        username = login_form.username.data
        user_data = get_user(username)

        user = UserAuthModel(user_data["id"], user_data["password"])

        login_user(user)

        return redirect(url_for("index"))

    context = {
        "login_form" : login_form
    }

    return render_template("login.html", **context)

@auth.route("/signup", methods=["GET","POST"])
def signup():

    signup_form = SignUpForm()

    if signup_form.validate_on_submit():

        username = signup_form.username.data
        password = generate_password_hash(signup_form.password.data)

        create_user(username, password)

        user = UserAuthModel(username, password)
        
        login_user(user)

        return redirect(url_for("index"))

    context = {
        "signup_form" : signup_form
    }

    return render_template("signup.html", **context)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
