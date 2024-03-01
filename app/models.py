from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

user_to_read = db.Table(
    'user_to_read',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.book_id'))
)

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    to_read_shelf = db.relationship('Book',
                             secondary=user_to_read,
                             backref="wants_to_read_by",
                             lazy="dynamic")

    def __init__ (self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_id(self):
        return (self.user_id)
    
class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    img_small = db.Column(db.String, nullable=True)
    img_large = db.Column(db.String, nullable=True)

    def __init__(self, title, author, img_small, img_large):
        self.title = title
        self.author = author
        self.img_small = img_small
        self.img_large = img_large

    def save(self):
        db.session.add(self)
        db.session.commit()