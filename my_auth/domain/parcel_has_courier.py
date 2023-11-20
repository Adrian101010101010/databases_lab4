from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class ParcelHasCourier(db.Model):
    courier_id = db.Column(db.BIGINT, db.ForeignKey('courier.id'), primary_key=True, nullable=False)
    parcel_id = db.Column(db.BIGINT, db.ForeignKey('parcel.id'), primary_key=True, nullable=False)
