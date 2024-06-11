from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms.widgets.core import TextArea
import re


def validate_slug(form, field):
    slug = field.data
    if not re.match(r'^[a-zA-Z0-9-]+$', slug):
        raise ValidationError("Slug must contain only letters, numbers, and hyphens.")


class PostForm(FlaskForm):
    title = StringField("title", [DataRequired("Please enter title."), Length(min=3, max=100)])
    content = StringField("content", [DataRequired("Please enter content.")], widget=TextArea())
    slug = StringField("slug", [DataRequired("Please enter slug."), validate_slug])
    submit = SubmitField("submit")
