from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Parcel(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    description = db.Column(db.String(45), nullable=False)
    weight = db.Column(db.String(45), nullable=False)
    status = db.Column(db.String(45), nullable=False)
    User_id = db.Column(db.BIGINT, db.ForeignKey('user.id'))
    couriers = relationship('Courier', secondary='parcel_has_courier', back_populates='parcels')
