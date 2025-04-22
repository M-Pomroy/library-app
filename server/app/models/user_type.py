from . import db

class UserType(db.Model):
    __tablename__ = 'user_type'

    type_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    type_description = db.Column(db.String(250))
    book_admin = db.Column(db.Boolean, default=False)
    tag_admin = db.Column(db.Boolean, default=False)
    user_admin = db.Column(db.Boolean, default=False)
    status_admin = db.Column(db.Boolean, default=False)

    users = db.relationship('User', backref="user_type", lazy=True)