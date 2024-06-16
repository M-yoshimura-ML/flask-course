from flask import render_template

from blueprints.admin import admin_bp
from blueprints.auth import auth_bp
from blueprints.post import post_bp
from blueprints.tests import test_bp
from blueprints.user import user_bp
from form.PostForm import SearchForm
from main import create_app

app = create_app()
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(post_bp, url_prefix="/post")
app.register_blueprint(auth_bp)
app.register_blueprint(test_bp)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html", error=e), 404


@app.context_processor
def inject_search_form():
    form = SearchForm()
    return dict(form=form)


if __name__ == "__main__":
    app.run()
