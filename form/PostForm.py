from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms.widgets.core import TextArea
import re

from models.post import Post


def validate_slug(form, field):
    slug = field.data
    if not re.match(r'^[a-zA-Z0-9-]+$', slug):
        raise ValidationError("Slug must contain only letters, numbers, and hyphens.")


def validate_unique_slug(form, field):
    slug = field.data
    post_id = form.post_id.data if 'post_id' in form else None
    print('post_id:', post_id)
    print('type of post_id:', type(post_id))
    existing_post = Post.query.filter_by(slug=slug).first()
    if existing_post and (post_id is None or existing_post.id != int(post_id)):
        raise ValidationError("This slug is already in use. Please choose different one.")


class PostForm(FlaskForm):
    title = StringField("title", [DataRequired("Please enter title."), Length(min=3, max=100)])
    content = StringField("content", [DataRequired("Please enter content.")], widget=TextArea())
    slug = StringField("slug", [DataRequired("Please enter slug."), validate_slug, validate_unique_slug])
    post_id = HiddenField("Post ID")
    submit = SubmitField("submit")
