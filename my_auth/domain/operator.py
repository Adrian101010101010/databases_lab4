from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Operator(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=True)
    surname = db.Column(db.String(45), nullable=True)
    phone = db.Column(db.String(45), nullable=True)
    Parcel_id = db.Column(db.BIGINT, ForeignKey('parcel.id'))
