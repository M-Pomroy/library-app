from . import db

class Status(db.Model):
    __tablename__ = 'status'

    status_id = db.Column(db.Integer, primary_key=True)
    status_name = db.Column(db.String(50), nullable=False)

    book_statuses = db.relationship('BookStatus', backref="status", lazy=True)