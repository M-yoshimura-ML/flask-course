from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect


csrf = CSRFProtect()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "YOUR_SECRET_KEY"
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flask_blog.db"
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost:port/db_name'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:password!123@localhost:3306/flask_blog'
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app


