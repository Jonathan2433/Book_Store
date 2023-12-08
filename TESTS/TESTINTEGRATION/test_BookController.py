# TESTS/TESTINTEGRATION/test_book_controller.py

import pytest
from flask import url_for
from APPLICATION.CONTROLLER.BookController import app as flask_app
from unittest.mock import patch

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        with flask_app.app_context():  # Ceci pousse un contexte d'application pour les tests
            yield client

@pytest.fixture
def mock_book_service():
    with patch('APPLICATION.SERVICE.BookService.BookService') as mock:
        yield mock

def test_get_books(client, mock_book_service):
    mock_book_service.return_value.list_books.return_value = [
        {'title': 'Book 1', 'author': 'Author 1'},
        {'title': 'Book 2', 'author': 'Author 2'}
    ]
    with flask_app.app_context():
        response = client.get(url_for('get_books'))
    assert response.status_code == 200
    assert len(response.json) == 2

def test_add_book(client, mock_book_service):
    book_data = {'title': 'New Book', 'author': 'New Author'}
    with flask_app.app_context():
        response = client.post(url_for('add_book'), json=book_data)
    assert response.status_code == 201
    mock_book_service.return_value.add_book.assert_called_once_with('New Book', 'New Author')
