import pytest
from APPLICATION.MODEL.Book import Book


def test_create_book_with_title_and_author():
    book = Book(title="1984", author="George Orwell")
    assert book.title == "1984"
    assert book.author == "George Orwell"


def test_create_book_without_title_should_raise_error():
    with pytest.raises(ValueError):
        Book(title="", author="George Orwell")


def test_create_book_without_author_should_raise_error():
    with pytest.raises(ValueError):
        Book(title="1984", author="")
