from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class CourierHasDelivery(db.Model):
    courier_id = db.Column(db.BIGINT, db.ForeignKey('courier.id'), primary_key=True, nullable=False)
    delivery_id = db.Column(db.BIGINT, db.ForeignKey('delivery.id'), primary_key=True, nullable=False)
