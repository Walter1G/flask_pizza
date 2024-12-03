from ..utils import db
from datetime import datetime

class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(45), nullable=False, unique=True)
    email=db.Column(db.String(50), nullable=False, unique=True)
    password_hash=db.Column(db.Text(), nullable=False)
    is_stagg=db.Column(db.Boolean(), default=False)
    is_active=db.Column(db.Boolean(),default=False)
    create_date=db.Column(db.DateTime(), default=datetime.utcnow)
    orders = db.relationship('Order',backref='customer',lazy=True)

    def __repr__(self) -> str:
        return f"<User {self.username}>"