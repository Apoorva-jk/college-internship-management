from app import app, db
from models.user import User


with app.app_context():

    existing_user = User.query.filter_by(
        username="admin"
    ).first()

    if existing_user:
        existing_user.set_password("admin124")
        db.session.commit()
        print(" admin password update successfully")
        
        print("Admin user already exists.")

    else:

        admin = User(
            username="admin",
            role="admin"
        )

        admin.set_password("admin124")

        db.session.add(admin)
        db.session.commit()

        print("Admin user created successfully.")