from . import db

class Format(db.Model):
    __tablename__ = 'format'

    format_id = db.Column(db.Integer, primary_key=True)
    format_type = db.Column(db.String(50), nullable=False)

    books = db.relationship('Book', backref='format', lazy=True)