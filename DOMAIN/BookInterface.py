from abc import ABC, abstractmethod
from typing import List
from APPLICATION.MODEL.Book import Book


class BookInterface(ABC):
    """
    An interface for a book repository, defining how to interact with the data layer.

    Methods:
        add_book(self, book: Book): Adds a new book to the repository.
        list_books(self) -> List[Book]: Retrieves all books from the repository.
    """

    @abstractmethod
    def add_book(self, book: Book):
        """
        Adds a new book to the repository.

        Parameters:
            book (Book): The book to add to the repository.
        """
        pass

    @abstractmethod
    def list_books(self) -> List[Book]:
        """
        Retrieves all books from the repository, sorted by title.

        Returns:
            List[Book]: The list of books.
        """
        pass
