# APPLICATION/__init__.py

from flask import Flask
from .CONTROLLER.BookController import app as book_controller
from .SERVICE.BookService import BookService
from DOMAIN.BookRepository import BookRepository

# Vous pourriez également initialiser votre BookService ici avec le repository
book_repository = BookRepository()
book_service = BookService(book_repository)

def create_app():
    app = Flask(__name__)
    app.book_service = book_service

    # Si vous utilisez des blueprints, enregistrez-les ici
    # app.register_blueprint(book_controller)

    # Si vous n'utilisez pas de blueprints et que vous avez défini vos routes directement sur 'app'
    # dans BookController.py, alors vous n'avez pas besoin d'enregistrer un blueprint,
    # et vous devriez simplement retourner 'book_controller' ici.
    return book_controller

# Maintenant, 'create_app' peut être importée et utilisée pour obtenir l'instance de l'application Flask
