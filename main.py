from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/hello/<name>')
def hello_world(name):
    return "Hello %s" %name


if __name__ == "__main__":
    app.run(debug=True)
