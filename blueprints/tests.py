from flask import Blueprint, render_template

test_bp = Blueprint('test', __name__, template_folder="templates")


@test_bp.route("/internal-error-test")
def internal_error_test():
    try:
        raise Exception("can't connect to Database.")
    except Exception as e:
        # abort(500)
        message = "Internal Server Error: " + str(e)
        # return Response(message, status=500)
        return internal_error(message)


@test_bp.errorhandler(500)
def internal_error(e):
    return render_template("errors/500.html", error=e), 500
