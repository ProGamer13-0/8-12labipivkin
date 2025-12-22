from app.models.book import db, Book
from app.models.repo import BookRepo

def test_create_book(repo):
    book = repo.add("Test Book", "Author")
    assert book.id is not None
    assert book.title == "Test Book"
    assert book.author == "Author"

def test_read_book(repo):
    book = repo.add("Read Book", "Author")
    retrieved = Book.query.get(book.id)
    assert retrieved.title == "Read Book"

def test_update_book(repo):
    book = repo.add("Old Title", "Author")
    book.title = "New Title"
    db.session.commit()
    updated = Book.query.get(book.id)
    assert updated.title == "New Title"

def test_delete_book(repo):
    book = repo.add("To Delete", "Author")
    book_id = book.id
    db.session.delete(book)
    db.session.commit()
    assert Book.query.get(book_id) is None
