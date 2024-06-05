from flask import Flask, render_template
from flask_wtf import CSRFProtect


csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "YOUR_SECRET_KEY"
    csrf.init_app(app)

    return app


