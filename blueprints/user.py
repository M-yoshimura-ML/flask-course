from flask import Blueprint, session, render_template, flash, redirect, url_for

from form.UserForm import AddUserForm

user_bp = Blueprint('user', __name__, template_folder="templates")


@user_bp.route('/profile/<name>')
def user_profile(name):
    if 'email' in session:
        name = session.get('username')
    return render_template('user/profile.html', name=name)


@user_bp.route('/add-user', methods=['GET', 'POST'])
def add_user():
    form = AddUserForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        session['username'] = username
        session['email'] = email
        flash("User is added successfully.")
        return redirect(url_for('user.user_profile', name=username))
    return render_template('user/add_user.html', form=form)
