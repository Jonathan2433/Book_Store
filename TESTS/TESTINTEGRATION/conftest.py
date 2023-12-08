import pytest
from APPLICATION.CONTROLLER.BookController import app as flask_app
from APPLICATION.SERVICE.BookService import BookService
from unittest.mock import create_autospec
from DOMAIN.BookRepository import BookRepository


@pytest.fixture
def book_service():
    book_repository = BookRepository()
    return BookService(book_repository)


@pytest.fixture
def client(book_service):
    # Inject the book service into the Flask app
    flask_app.config['TESTING'] = True
    flask_app.book_service = book_service
    with flask_app.test_client() as client:
        yield client


@pytest.fixture
def book_service_mock():
    # Create a mock for the BookService
    return create_autospec(BookService)