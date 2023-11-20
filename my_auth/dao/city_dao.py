from my_auth.domain.city import City
from app.app import db


class CityDAO:

    @staticmethod
    def add_cities():
        cities_data = [
            (1, 'Lviv'),
            (2, 'Stryi'),
            (3, 'Kyiv'),
            (4, 'Ternopil'),
            (5, 'Zakarpattya'),
            (6, 'Kharkiv'),
            (7, 'Odessa'),
            (8, 'Poltava'),
            (9, 'Vinnytsia'),
            (10, 'Chernihiv')
        ]

        for city_id, city_name in cities_data:
            city = City(id=city_id, city_name=city_name)
            db.session.add(city)

        db.session.commit()

    @staticmethod
    def create_city(city_name, regione_name):
        city = City(city_name=city_name, regione_name=regione_name)
        db.session.add(city)
        db.session.commit()
        return city

    @staticmethod
    def get_city_by_id(city_id):
        return City.query.get(city_id)

    @staticmethod
    def get_all_cities():
        return City.query.all()

    @staticmethod
    def update_city(city_id, city_name, regione_name):
        city = City.query.get(city_id)
        if city:
            city.city_name = city_name
            city.regione_name = regione_name
            db.session.commit()
            return city
        return None

    @staticmethod
    def delete_city(city_id):
        city = City.query.get(city_id)
        if city:
            db.session.delete(city)
            db.session.commit()
            return city
        return None

    @staticmethod
    def init_app(app):
        db.init_app(app)
        with app.app_context():
            db.create_all()
