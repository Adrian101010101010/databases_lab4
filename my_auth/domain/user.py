from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(45), nullable=False)
    birthday = db.Column(db.DATE, nullable=False)
    place_of_delivery = db.Column(db.String(45), nullable=False)
    parcels = relationship('Parcel', backref='user')
