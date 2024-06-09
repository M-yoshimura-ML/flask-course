import datetime

from flask import Blueprint, render_template, flash, redirect
from flask_login import login_required

from form.UserForm import UpdateUserForm
from main import db
from models.user import User

user_bp = Blueprint('user', __name__, template_folder="templates")


@user_bp.route('/profile')
@login_required
def user_profile():
    return render_template('user/profile.html')


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
