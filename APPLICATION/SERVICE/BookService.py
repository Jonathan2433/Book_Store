from APPLICATION.MODEL.Book import Book
from typing import List
from DOMAIN.BookInterface import BookInterface


class BookService:
    """
    A service class that provides use cases for managing books.

    Attributes:
        book_repository (BookRepositoryInterface): The repository interface for books.

    Methods:
        add_book(self, title: str, author: str): Adds a new book to the repository.
        list_books(self) -> List[Book]: Lists all books in the repository, sorted by title.
    """
    def __init__(self, book_repository: BookInterface):
        """
        Constructs all the necessary attributes for the book service object.

        Parameters:
            book_repository (BookRepositoryInterface): The repository interface for books.
        """
        self.book_repository = book_repository

    def add_book(self, title: str, author: str):
        """
        Adds a new book with the given title and author to the repository.

        Parameters:
            title (str): The title of the book.
            author (str): The author of the book.

        Raises:
            ValueError: If 'title' or 'author' is empty.
        """
        book = Book(title, author)
        self.book_repository.add_book(book)

    def list_books(self) -> List[Book]:
        """
        Lists all the books in the repository, sorted by their title.

        Returns:
            List[Book]: The list of books, sorted by title.
        """
        return self.book_repository.list_books()

