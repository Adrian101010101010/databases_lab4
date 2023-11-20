from my_auth.domain.regione import Regione
from app.app import db


class RegioneDAO:
    @staticmethod
    def add_regioni():
        regioni_data = [
            ('Lviv region'),
            ('Kyiv region'),
            ('Zakarpattya region'),
            ('Volyn region'),
            ('Ternopil region'),
            ('Kharkiv region'),
            ('Odessa region'),
            ('Poltava region'),
            ('Vinnytsia region'),
            ('Chernihiv region')
        ]

        # Додати значення в таблицю regione
        for name in regioni_data:
            regione = Regione(name=name)
            db.session.add(regione)

        # Зберегти зміни в базі даних
        db.session.commit()
    @staticmethod
    def create_regione(name):
        regione = Regione(name=name)
        db.session.add(regione)
        db.session.commit()
        return regione

    @staticmethod
    def get_regione_by_name(name):
        return Regione.query.get(name)

    @staticmethod
    def get_all_regioni():
        return Regione.query.all()

    @staticmethod
    def update_regione(name, new_name):
        regione = Regione.query.get(name)
        if regione:
            regione.name = new_name
            db.session.commit()
            return regione
        return None

    @staticmethod
    def delete_regione(name):
        regione = Regione.query.get(name)
        if regione:
            db.session.delete(regione)
            db.session.commit()
            return regione
        return None

    @staticmethod
    def init_app(app):
        db.init_app(app)
        with app.app_context():
            db.create_all()
