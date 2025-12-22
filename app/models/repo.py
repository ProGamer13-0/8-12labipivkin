from .book import Book, db

class BookRepo:
    def __init__(self, db_instance=None):
        if db_instance:
            global db
            db = db_instance

    def all(self):
        return Book.query.all()

    def add(self, title, author):
        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()
        return new_book
