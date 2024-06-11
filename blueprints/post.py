from flask import Blueprint, render_template, flash

from form.PostForm import PostForm
from main import db
from models.post import Post

post_bp = Blueprint('post', __name__, template_folder='templates')


@post_bp.route('/add-post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        slug = form.slug.data
        post = Post(title=title, content=content, slug=slug)
        try:
            db.session.add(post)
            db.session.commit()
            form.title.data = ''
            form.content.data = ''
            form.slug.data = ''
            flash("New Post is created successfully.")
        except:
            flash("There is something wrong to create post.")
    return render_template('post/add_post.html', form=form)


@post_bp.route('/post-list', methods=['GET', 'POST'])
def post_list():
    posts = Post.query.order_by(Post.created_at)
    return render_template('post/post_list.html', posts=posts)
