from my_auth.domain.operator import Operator
from app.app import db


class OperatorDAO:
    @staticmethod
    def add_operators():
        operators_data = [
            (1, 'Andriy', 'Kub', '+380(75) 856 12 49'),
            (2, 'Zak', 'Kohtr', '+380(38)380 38 00'),
            (3, 'Petro', 'Petrok', '+380(99)999 99 99'),
            (4, 'Ostap', 'Holodnic', '+380(11)111 11 12'),
            (5, 'Igor', 'Plich', '+380(32)953 45 55'),
            (6, 'Artur', 'Melnyk', '+380(59)137 62 81'),
            (7, 'Vitaly', 'Koval', '+380(94)796 91 64'),
            (8, 'Tetyana', 'Cap', '+380(95)495 26 35'),
            (9, 'Natalia', 'Dor', '+380(55)555 55 55'),
            (10, 'Oksana', 'Sydorenko', '+380(75)861 95 13')
        ]

        # Додати значення в таблицю operator
        for operator_data in operators_data:
            operator = Operator(
                id=operator_data[0],
                name=operator_data[1],
                surname=operator_data[2],
                phone=operator_data[3]
            )
            db.session.add(operator)

        # Зберегти зміни в базі даних
        db.session.commit()

    @staticmethod
    def create_operator(name, surname, phone, parcel_id):
        operator = Operator(name=name, surname=surname, phone=phone, Parcel_id=parcel_id)
        db.session.add(operator)
        db.session.commit()
        return operator

    @staticmethod
    def get_operator_by_id(operator_id):
        return Operator.query.get(operator_id)

    @staticmethod
    def get_all_operators():
        return Operator.query.all()

    @staticmethod
    def update_operator(operator_id, name, surname, phone, parcel_id):
        operator = Operator.query.get(operator_id)
        if operator:
            operator.name = name
            operator.surname = surname
            operator.phone = phone
            operator.Parcel_id = parcel_id
            db.session.commit()
            return operator
        return None

    @staticmethod
    def delete_operator(operator_id):
        operator = Operator.query.get(operator_id)
        if operator:
            db.session.delete(operator)
            db.session.commit()
            return operator
        return None

    @staticmethod
    def init_app(app):
        db.init_app(app)
        with app.app_context():
            db.create_all()
