from flask import Blueprint, render_template

from form.PostForm import PostForm

post_bp = Blueprint('post', __name__, template_folder='templates')


@post_bp.route('/add-post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    return render_template('post/add_post.html', form=form)
