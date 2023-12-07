from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from app import app, db
from models import User, Image


class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin == True


class AdminHomeView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin == True


admin = Admin(app, index_view=AdminHomeView())
admin.add_view(AdminModelView(User, db.session))
admin.add_view(AdminModelView(Image, db.session))
