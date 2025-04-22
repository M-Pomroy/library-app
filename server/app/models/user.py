from . import db

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    mobile = db.Column(db.String(20))
    postcode = db.Column(db.String(10))
    type_id = db.Column(db.Integer, db.ForeignKey('user_type.type_id'), nullable=False)

    book_statuses = db.relationship('BookStatus', backref='user', lazy=True)