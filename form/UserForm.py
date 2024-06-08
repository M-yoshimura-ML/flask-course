from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class AddUserForm(FlaskForm):
    username = StringField("User Name", [DataRequired("Please enter user name.")])
    email = StringField("Email", [DataRequired("please enter email address."),
                                  Email("Please enter proper email address.")])
    password = PasswordField("Password", [DataRequired("Please enter password.")])
    password2 = PasswordField("Password Confirm",
                              validators=[DataRequired("Please enter password."),
                                          EqualTo('password', message='Password Confirm must match with password.')])
    submit = SubmitField("Send")


class UpdateUserForm(FlaskForm):
    username = StringField("User Name", [DataRequired("Please enter user name.")])
    address = StringField("Address")
    submit = SubmitField("Update")


class LoginForm(FlaskForm):
    email = StringField("Email", [DataRequired("please enter email address."),
                                  Email("Please enter proper email address.")])
    password = PasswordField("Password", [DataRequired("Please enter password.")])
    submit = SubmitField("Login")