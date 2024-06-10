from flask import render_template

from blueprints.admin import admin_bp
from blueprints.auth import auth_bp
from blueprints.post import post_bp
from blueprints.tests import test_bp
from blueprints.user import user_bp
from main import create_app

app = create_app()
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(post_bp, url_prefix="/post")
app.register_blueprint(auth_bp)
app.register_blueprint(test_bp)


@app.route('/')
def hello():
    name = 'masa'
    posts = [
        {'title': 'test1', 'author': 'masa'},
        {'title': 'test2', 'author': 'john'}
    ]
    return render_template('hello.html', name=name, posts=posts)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html", error=e), 404


if __name__ == "__main__":
    app.run(debug=True)
