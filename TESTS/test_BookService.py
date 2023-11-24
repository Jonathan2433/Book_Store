from APPLICATION.SERVICE.BookService import BookService
from APPLICATION.MODEL.Book import Book
from hypothesis import given, strategies as st


class InMemoryBookRepository:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return sorted(self.books, key=lambda book: book.title)


def test_add_book():
    book_repository = InMemoryBookRepository()
    book_service = BookService(book_repository)

    book_service.add_book("1984", "George Orwell")
    assert book_repository.list_books()[0].title == "1984"


def test_list_books_in_alphabetical_order():
    book_repository = InMemoryBookRepository()
    book_service = BookService(book_repository)

    book_service.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    book_service.add_book("1984", "George Orwell")
    book_service.add_book("Animal Farm", "George Orwell")

    books = book_service.list_books()
    assert books[0].title == "1984"
    assert books[1].title == "Animal Farm"
    assert books[2].title == "The Great Gatsby"


# Test de la création valide d'un livre
@given(title=st.text(min_size=1), author=st.text(min_size=1))
def test_create_book_with_non_empty_title_and_author(title, author):
    book = Book(title, author)
    assert book.title == title
    assert book.author == author


# Test de l'ordre alphabétique de la liste des livres
@given(st.lists(st.tuples(st.text(min_size=1), st.text(min_size=1)), unique_by=lambda x: x[0]))
def test_list_books_in_alphabetical_order(books_data):
    book_repository = InMemoryBookRepository()
    book_service = BookService(book_repository)

    for title, author in books_data:
        book_service.add_book(title, author)

    books = book_service.list_books()
    assert books == sorted(books, key=lambda book: book.title)


# Test d'absence de doublons dans la liste des livres
@given(st.lists(st.tuples(st.text(min_size=1), st.text(min_size=1)), unique_by=lambda x: x[0]))
def test_list_books_has_no_duplicates(books_data):
    book_repository = InMemoryBookRepository()
    book_service = BookService(book_repository)

    for title, author in books_data:
        book_service.add_book(title, author)

    books = book_service.list_books()
    titles = [book.title for book in books]
    assert len(titles) == len(set(titles))