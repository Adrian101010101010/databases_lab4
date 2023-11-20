from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Department(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    location = db.Column(db.String(45), nullable=False)
    number = db.Column(db.String(45), nullable=False)
    contacts = db.Column(db.String(45), nullable=False)
    city_id = db.Column(db.BIGINT, db.ForeignKey('city.id'))
    User_id = db.Column(db.BIGINT, db.ForeignKey('user.id'))

