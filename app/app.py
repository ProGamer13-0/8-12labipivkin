from flask import Flask, render_template
from flask_login import LoginManager
from .controllers.books_controller import bp as books_bp
from .controllers.auth_controller import bp as auth_bp
from .models.book import db, Book
from .models.user import User, UserRepo

app = Flask(__name__, template_folder="views", static_folder="static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask_user:123@localhost/flask_db'
app.config['SECRET_KEY'] = 'your_secret_key_here'

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(books_bp)
app.register_blueprint(auth_bp)

# Стартовая страница
@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

# Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Создаём admin, если нет
with app.app_context():
    repo = UserRepo()
    if not repo.get_by_username('admin'):
        repo.add('admin', 'password123')

if __name__ == "__main__":
    app.run(debug=True)
