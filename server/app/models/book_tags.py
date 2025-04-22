from . import db
from .tag import Tag
from .book import Book

class BookTags(db.Model):
    __tablename__ = 'book_tags'

    tag_id = db.Column(db.Integer, db.ForeignKey('tag.tag_id'), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), primary_key=True)