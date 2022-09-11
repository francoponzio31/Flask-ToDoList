from flask import render_template
from flask_login import login_required, current_user
from app import create_app

app = create_app()

@app.route("/", methods=["GET","POST"])
@login_required
def index():
    
    username = current_user.id

    context = {
        "username" : username
    }

    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run()