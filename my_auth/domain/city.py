from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class City(db.Model):
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    city_name = db.Column(db.String(45), nullable=False)
    regione_name = db.Column(db.String(50), db.ForeignKey('regione.name'))
    department = relationship('Department', backref='city')
