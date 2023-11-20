from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Courier(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=True)
    surname = db.Column(db.String(45), nullable=True)
    phone = db.Column(db.String(45), nullable=True)
    birthday = db.Column(db.DATE, nullable=False)
    parcels = relationship('Parcel', secondary='parcel_has_courier', back_populates='couriers')
    deliveries = relationship('Delivery', secondary='courier_has_delivery', back_populates='couriers')
