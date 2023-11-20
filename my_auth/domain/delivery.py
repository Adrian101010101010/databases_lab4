from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Delivery(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    recipient = db.Column(db.String(45), nullable=True)
    cargo_volume = db.Column(db.String(45), nullable=True)
    User_id = db.Column(db.BIGINT, db.ForeignKey('user.id'))
