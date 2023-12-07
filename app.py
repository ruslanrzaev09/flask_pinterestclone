from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app = Flask(__name__, static_url_path="/static")

app.config["SECRET_KEY"] = "r273gtwrhestjhuiagt877g9h8u"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///imageApp_db.db"

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"
