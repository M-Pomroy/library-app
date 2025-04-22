from . import db

class Tag(db.Model):
    __tablename__ = 'tag'

    tag_id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(50), nullable=False)

    books = db.relationship('Book', secondary='book_tags', backref='tags', lazy=True)