from APPLICATION.MODEL.Book import Book
from APPLICATION.SERVICE.BookService import BookService

book = Book('hola', 'bg')
service = BookService(2)
print(service.list_books())