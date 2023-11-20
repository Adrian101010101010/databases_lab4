from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()



class Regione(db.Model):
    name = db.Column(db.String(50), primary_key=True)
    city = relationship('City', backref='regione')
