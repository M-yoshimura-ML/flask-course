from flask import Flask, render_template, abort, Response, request, redirect, url_for, session, flash
from flask_wtf import CSRFProtect

from blueprints.tests import test_bp
from blueprints.user import user_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = "YOUR_SECRET_KEY"
csrf = CSRFProtect(app)
app.register_blueprint(user_bp, url_prefix="/user")
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
