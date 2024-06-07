from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class AddUserForm(FlaskForm):
    username = StringField("User Name", [DataRequired("Please enter user name.")])
    email = StringField("Email", [DataRequired("please enter email address."),
                                  Email("Please enter proper email address.")])
    password = PasswordField("Password", [DataRequired("Please enter password.")])
    submit = SubmitField("Send")


class UpdateUserForm(FlaskForm):
    username = StringField("User Name", [DataRequired("Please enter user name.")])
    submit = SubmitField("Update")
