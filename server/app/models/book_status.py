from . import db

class BookStatus(db.Model):
    __tablename__ = 'book_status'

    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), primary_key=True)
    status_id = db.Column(db.Integer, db.ForeignKey('status.status_id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    timestamp = db.Column(db.DateTime)