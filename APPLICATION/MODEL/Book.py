class Book:
    """
    A class to represent a book.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.

    Methods:
        __init__(self, title: str, author: str): Initializes a new book instance.
    """

    def __init__(self, title: str, author: str):
        """
        Construct all the necessary attributes for the book object.

        Parameters:
            title (str): The title of the book, must be non-empty.
            author (str): The author of the book, must be non-empty.

        Raises:
            ValueError: If 'title' or 'author' is empty.
        """
        if not title:
            raise ValueError("Book title cannot be empty")
        if not author:
            raise ValueError("Book author cannot be empty")
        self.title = title
        self.author = author
