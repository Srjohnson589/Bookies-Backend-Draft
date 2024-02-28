from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__ (self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_id(self):
        return (self.user_id)