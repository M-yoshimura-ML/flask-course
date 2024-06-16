import logging
import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect


csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flask_blog.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')

    if not app.debug:
        app.logger.setLevel(logging.INFO)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)

    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    with app.app_context():
        db.create_all()

    app.logger.info("Flask app created and initialized.")
    return app


