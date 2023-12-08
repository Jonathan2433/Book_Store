# APPLICATION/CONTROLLER/BookController.py

from flask import Flask, jsonify, request
from DTO.bookDTO import BookDTO
from APPLICATION.SERVICE.BookService import BookService
from DOMAIN.BookRepository import BookRepository

app = Flask(__name__)

# Créez une instance de BookRepository
book_repository = BookRepository()
# Injectez BookRepository dans BookService
book_service = BookService(book_repository)

@app.route('/books', methods=['GET'])
def get_books():
    books = book_service.list_books()
    books_dto = [BookDTO(book.title, book.author).to_dict() for book in books]
    return jsonify(books_dto), 200


@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    book_dto = BookDTO(title=data['title'], author=data['author'])
    book_service.add_book(book_dto.title, book_dto.author)
    return jsonify(book_dto.to_dict()), 201
