from flask import Blueprint, request, render_template, redirect, url_for
from ..models.repo import BookRepo
from ..models.book import db, Book
from flask_login import login_required

bp = Blueprint("books", __name__, url_prefix="/books")
repo = BookRepo(db)

# ------------------------------
# Список всех книг
# ------------------------------
@bp.get("/")
@login_required
def list_books():
    books = repo.all()
    return render_template("list.html", books=books)

# ------------------------------
# Добавление новой книги
# ------------------------------
@bp.route("/create", methods=["GET", "POST"])
@login_required
def create_book():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        repo.add(title, author)
        return redirect(url_for("books.list_books"))
    # GET-запрос: просто отображаем форму
    return render_template("book_form.html", book=None)

# ------------------------------
# Редактирование существующей книги
# ------------------------------
@bp.route("/<int:book_id>/edit", methods=["GET", "POST"])
@login_required
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == "POST":
        book.title = request.form.get("title", book.title)
        book.author = request.form.get("author", book.author)
        db.session.commit()
        return redirect(url_for("books.list_books"))
    # GET-запрос: отображаем форму с данными книги
    return render_template("book_form.html", book=book)

# ------------------------------
# Удаление книги
# ------------------------------
@bp.post("/<int:book_id>/delete")
@login_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("books.list_books"))
