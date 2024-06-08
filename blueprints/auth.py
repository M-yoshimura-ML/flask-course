from flask import Blueprint, session, flash, redirect, url_for, render_template

from form.UserForm import AddUserForm, LoginForm
from main import db
from models.user import User

auth_bp = Blueprint('auth', __name__, template_folder="templates")


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = AddUserForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user is None:
            user = User(name=username, email=email)
            user.password = password
            db.session.add(user)
            db.session.commit()
            session['username'] = username
            session['email'] = email
            flash("Signup is successful.")
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)
