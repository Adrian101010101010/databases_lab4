# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from my_auth.dao.department_dao import DepartmentDAO
from my_auth.dao.city_dao import CityDAO
from my_auth.dao.user_dao import UserDAO
from my_auth.dao.courier_dao import CourierDAO
from my_auth.dao.delivery_dao import DeliveryDAO
from my_auth.dao.operator_dao import OperatorDAO
from my_auth.dao.parcel_dao import ParcelDAO
from my_auth.dao.regione_dao import RegioneDAO
# Імпортуйте інші DAO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{user}:{password}@{host}:{port}/{database}'.format(
    user=DB_CONFIG['user'],
    password=DB_CONFIG['password'],
    host=DB_CONFIG['host'],
    port=DB_CONFIG['port'],
    database=DB_CONFIG['database']
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Ініціалізуйте бази даних
DepartmentDAO.init_app(app)
CityDAO.init_app(app)
UserDAO.init_app(app)
CourierDAO.init_app(app)
DeliveryDAO.init_app(app)
OperatorDAO.init_app(app)
ParcelDAO.init_app(app)
RegioneDAO.init_app(app)

db = SQLAlchemy()
db.init_app(app)
# Ініціалізуйте інші бази даних
