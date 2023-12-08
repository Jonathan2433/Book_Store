# DOMAIN/BookRepository.py

from DOMAIN.BookInterface import BookInterface
from APPLICATION.MODEL.Book import Book


class BookRepository(BookInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        return sorted(self.books, key=lambda book: book.title)
