from flask import Flask
from config import Config
from flask_login import LoginManager
from app.models import db, User
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager()

login_manager.init_app(app)
db.init_app(app)
migrate = Migrate(app, db)

from app.blueprints.auth_api import auth_api

app.register_blueprint(auth_api)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)