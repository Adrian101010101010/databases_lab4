from my_auth.domain.courier import Courier
from app.app import db


class CourierDAO:
    @staticmethod
    def add_couriers():
        couriers_data = [
            (1, 'Artur', 'Cap', '+380(45)786 45 29', '2001-10-24'),
            (2, 'Panas', 'Madrid', '+380(78)496 79 45', '1988-06-3'),
            (3, 'Zak', 'Luk', '+380(67)364 46 63', '1999-09-09'),
            (4, 'Dgon', 'Karter', '+380(55)762 35 76', '2000-12-20'),
            (5, 'Andriy', 'Dor', '+380(49)486 72 92', '2002-02-02'),
            (6, 'Ivan', 'Petrov', '+380(11)123 45 67', '1995-03-17'),
            (7, 'Marina', 'Sydorenko', '+380(68)987 12 34', '1990-08-25'),
            (8, 'Olexandr', 'Ivanov', '+380(50)555 99 77', '1985-02-10'),
            (9, 'Tetyana', 'Koval', '+380(99)777 11 88', '1992-11-29'),
            (10, 'Andriy', 'Melnyk', '+380(44)321 76 54', '1998-06-03')
        ]

        for courier_data in couriers_data:
            courier = Courier(
                id=courier_data[0],
                name=courier_data[1],
                surname=courier_data[2],
                phone=courier_data[3],
                birthday=courier_data[4]
            )
            db.session.add(courier)

        db.session.commit()

    @staticmethod
    def create_courier(name, surname, phone, birthday):
        courier = Courier(name=name, surname=surname, phone=phone, birthday=birthday)
        db.session.add(courier)
        db.session.commit()
        return courier

    @staticmethod
    def get_courier_by_id(courier_id):
        return Courier.query.get(courier_id)

    @staticmethod
    def get_all_couriers():
        return Courier.query.all()

    @staticmethod
    def update_courier(courier_id, name, surname, phone, birthday):
        courier = Courier.query.get(courier_id)
        if courier:
            courier.name = name
            courier.surname = surname
            courier.phone = phone
            courier.birthday = birthday
            db.session.commit()
            return courier
        return None

    @staticmethod
    def delete_courier(courier_id):
        courier = Courier.query.get(courier_id)
        if courier:
            db.session.delete(courier)
            db.session.commit()
            return courier
        return None

    @staticmethod
    def init_app(app):
        db.init_app(app)
        with app.app_context():
            db.create_all()
