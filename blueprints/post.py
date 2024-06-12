from flask import Blueprint, render_template, flash, abort

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


@post_bp.route('/post-list', methods=['GET'])
def post_list():
    posts = Post.query.order_by(Post.created_at)
    return render_template('post/post_list.html', posts=posts)


@post_bp.route('/view-post/<slug>', methods=['GET'])
def view_post(slug):
    post = Post.query.filter_by(slug=slug).first()
    if not post:
        abort(404)
    return render_template('post/view_post.html', post=post)


@post_bp.route('/update-post/<id>', methods=['GET', 'POST'])
def update_post(id):
    post = Post.query.get_or_404(id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.slug = form.slug.data
        try:
            db.session.add(post)
            db.session.commit()
            flash("Post has been updated successfully.")
        except:
            flash("There is something wrong to update post.")
    else:
        form.title.data = post.title
        form.content.data = post.content
        form.slug.data = post.slug
    return render_template("post/update_post.html", form=form, post=post, id=id)
