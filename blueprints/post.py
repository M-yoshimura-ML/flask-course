import os

from flask import Blueprint, render_template, flash, abort, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from google.cloud import storage
from sqlalchemy import desc
from werkzeug.utils import secure_filename

from form.PostForm import PostForm, SearchForm
from main import db, csrf
from models.post import Post

post_bp = Blueprint('post', __name__, template_folder='templates')


@post_bp.route('/add-post', methods=['GET', 'POST'])
@login_required
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        slug = form.slug.data
        user_id = current_user.id
        post = Post(title=title, content=content, slug=slug, user_id=user_id)
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
    page = request.args.get('page', 1, type=int)
    per_page = 5
    posts = Post.query.order_by(Post.created_at).paginate(page=page, per_page=per_page, error_out=False)
    return render_template('post/post_list.html', posts=posts)


@post_bp.route('/view-post/<slug>', methods=['GET'])
def view_post(slug):
    post = Post.query.filter_by(slug=slug).first()
    if not post:
        abort(404)
    return render_template('post/view_post.html', post=post)


def own_user_check(post, message):
    if not (post.user_id == current_user.id):
        flash(message=message)
        return redirect(url_for('post.post_list'))


@post_bp.route('/update-post/<id>', methods=['GET', 'POST'])
@login_required
def update_post(id):
    post = Post.query.get_or_404(id)
    form = PostForm()
    message = "You do not have permission to edit the blog."
    user_check_result = own_user_check(post, message)
    if user_check_result:
        return user_check_result
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
        form.post_id.data = post.id
    return render_template("post/update_post.html", form=form, id=id)


@post_bp.route('/delete-post/<id>', methods=['GET'])
@login_required
def delete_post(id):
    post = Post.query.get_or_404(id)
    message = "You do not have permission to delete the blog."
    user_check_result = own_user_check(post, message)
    if user_check_result:
        return user_check_result
    try:
        db.session.delete(post)
        db.session.commit()
        flash("Post is deleted successfully.")
    except:
        flash("There is something wrong to delete post.")
    return redirect(url_for('post.post_list'))


@post_bp.route('/upload', methods=['POST'])
@csrf.exempt
def upload():
    f = request.files.get('upload')
    if f:
        filename = secure_filename(f.filename)
        client = storage.Client()
        bucket = client.get_bucket(os.environ.get('BUCKET_NAME'))
        blob = bucket.blob('images/uploads/' + filename)
        blob.upload_from_file(f, content_type=f.content_type)
        blob.make_public()
        url = blob.public_url
        # filepath = os.path.join('static/images/uploads/' + filename)
        # f.save(filepath)
        # url = url_for('static', filename='images/uploads/' + filename)
        return jsonify({"uploaded": 1, "filename": filename, "url": url})
    return jsonify({"uploaded": 0, "error": {"message": "upload failed"}})


@post_bp.route('/search', methods=['POST'])
def search():
    form = SearchForm()
    searched = form.searched.data
    if form.validate_on_submit():
        posts = Post.query.filter(Post.content.like('%' + searched + '%')).order_by(desc(Post.created_at)).all()
        return render_template('post/search_post.html', form=form, searched=searched, posts=posts)

