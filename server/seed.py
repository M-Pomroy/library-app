from app import create_app
from app.models import db
from app.models.format import Format

app = create_app()

with app.app_context():
    db.session.query(Format).delete()

    paperback = Format(format_id=0, format_type="Paperback")
    hardback = Format(format_id=1, format_type="Hardback")
    eBook = Format(format_id=2, format_type="EBook")

    db.session.add_all([paperback, hardback, eBook])
    db.session.commit()

    print("Seed data inserted")