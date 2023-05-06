from app import *

with app.app_context():
    db.create_all()
    user = User(name = "Roman", username = "r12345", password = "123456")
    db.session.add(user)
    db.session.commit()