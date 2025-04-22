from app import create_app
from app.models import db
from app.models import format, book, tag, book_tags, user_type, user, status, book_status

app = create_app()

with app.app_context():
    db.create_all()
    print("Tables created successfully!")