import datetime

from flask import Blueprint, session, render_template, flash, redirect, url_for
from flask_login import login_required

from form.UserForm import AddUserForm, UpdateUserForm
from main import db
from models.user import User

user_bp = Blueprint('user', __name__, template_folder="templates")


@user_bp.route('/profile/<name>')
@login_required
def user_profile(name):
    if 'email' in session:
        name = session.get('username')
    return render_template('user/profile.html', name=name)


@user_bp.route('/add-user', methods=['GET', 'POST'])
@login_required
def add_user():
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
            flash("User is added successfully.")
        return redirect(url_for('user.user_profile', name=username))
    users = User.query.order_by(User.created_at)
    return render_template('user/add_user.html', form=form, user_list=users)


@user_bp.route("/update-user/<int:id>", methods=['GET', 'POST'])
@login_required
def update_user(id):
    form = UpdateUserForm()
    user = User.query.get_or_404(id)
    if form.validate_on_submit():
        user.name = form.username.data
        user.address = form.address.data
        user.updated_at = datetime.datetime.now()
        try:
            db.session.commit()
            flash("User is updated successfully.")
        except:
            flash("Error looks like there was a problem.")
    return render_template("user/update_user.html", form=form, user=user)


@user_bp.route("/delete/<int:id>")
@login_required
def delete_user(id):
    user = User.query.get_or_404(id)
    try:
        db.session.delete(user)
        db.session.commit()
        flash("User is deleted successfully.")
    except:
        flash("There was a problem to delete user.")
    return redirect('/user/add-user')
