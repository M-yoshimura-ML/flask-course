from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    name = 'masa'
    posts = [
        {'title': 'test1', 'author': 'masa'},
        {'title': 'test2', 'author': 'john'}
    ]
    return render_template('hello.html', name=name, posts=posts)


@app.route('/profile/<name>')
def user_profile(name):
    return render_template('user/profile.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)
