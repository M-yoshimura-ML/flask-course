from flask import Flask, render_template, abort, Response, request, redirect, url_for, session, flash
from flask_wtf import CSRFProtect

from blueprints.user import user_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = "YOUR_SECRET_KEY"
csrf = CSRFProtect(app)
app.register_blueprint(user_bp)


@app.route('/')
def hello():
    name = 'masa'
    posts = [
        {'title': 'test1', 'author': 'masa'},
        {'title': 'test2', 'author': 'john'}
    ]
    return render_template('hello.html', name=name, posts=posts)


@app.route("/internal-error-test")
def internal_error_test():
    try:
        raise Exception("can't connect to Database.")
    except Exception as e:
        # abort(500)
        message = "Internal Server Error: " + str(e)
        # return Response(message, status=500)
        return internal_error(message)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html", error=e), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template("errors/500.html", error=e), 500


if __name__ == "__main__":
    app.run(debug=True)
