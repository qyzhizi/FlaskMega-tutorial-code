from flask import Flask
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from config import Config

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder=Config.EMPLATE_DIR)
app.config.from_object(Config)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login = LoginManager(app)
mail = Mail(app)

login.login_view = 'login'
login.login_message = 'You must login to access this page'
login.login_message_category = 'info'

from application.routes import *