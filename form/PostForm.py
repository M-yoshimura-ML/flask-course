from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets.core import TextArea


class PostForm(FlaskForm):
    title = StringField("title", [DataRequired("Please enter title.")])
    content = StringField("content", [DataRequired("Please enter content.")], widget=TextArea())
    slug = StringField("slug", [DataRequired("Please enter slug.")])
    submit = SubmitField("submit")
