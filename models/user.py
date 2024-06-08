from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from main import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    # password = db.Column(db.String(200), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return self.name + ' san'

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute.")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
