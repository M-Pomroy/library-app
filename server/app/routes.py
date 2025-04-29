from flask import Blueprint, request, jsonify
from flask_cors import CORS
from .models.book import Book

api = Blueprint('api', __name__)
CORS(api, origins=["http://localhost:5173"])

@api.route('/api/hello', methods=["GET"])
def hello():
    return jsonify(message="Hello World")

@api.route('/api/addBook', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(
        title = data['title'],
        author = data['author'],
        book_description = data['description'],
        release_date = data['releaseDate'],
        ISBN = data['isbn'],
        format_id = data['format'],
    )
    new_book.save()
    return jsonify(message="Book added successfully"), 201

@api.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book:
        book.delete()
        return jsonify(message="Book deleted"), 200
    return jsonify(error="Book not found"), 404
