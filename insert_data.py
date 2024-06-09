from main import db, create_app
from models.user import Role, User


app = create_app()


with app.app_context():
    if not Role.query.filter_by(name='admin').first():
        admin_role = Role(name='admin')
        db.session.add(admin_role)
    if not Role.query.filter_by(name='user').first():
        user_role = Role(name='user')
        db.session.add(user_role)

    admin = User.query.filter_by(email='admin@gmail.com').first()
    if admin:
        admin.role_id = 1
    db.session.commit()
