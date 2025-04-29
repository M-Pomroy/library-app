from . import db
from .format import Format
from .tag import Tag

class Book(db.Model):
    __tablename__ = 'book'

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    book_description = db.Column(db.String(250))
    release_date = db.Column(db.Date)
    ISBN = db.Column(db.String(17))
    format_id = db.Column(db.Integer, db.ForeignKey('format.format_id'), nullable=False)

    #tags = db.relationship('Tag', secondary='book_tags', backref='books', lazy=True)

    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"

    # Utility Methods
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()