
from flask import Blueprint, flash, redirect, url_for, session, render_template
from flask_login import current_user, login_required

from form.UserForm import AddUserForm
from main import db
from models.user import User

admin_bp = Blueprint('admin', __name__, template_folder='templates')


def admin_check():
    if current_user.role.name != 'admin':
        flash("You do not have permission to access this page.")
        return redirect(url_for('auth.dashboard'))


@admin_bp.route('/add-user', methods=['GET', 'POST'])
@login_required
def add_user():
    check_result = admin_check()
    if check_result:
        return check_result

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
        return redirect(url_for('admin.add_user'))
    users = User.query.order_by(User.created_at)
    return render_template('admin/add_user.html', form=form, user_list=users)
