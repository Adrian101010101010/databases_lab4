from my_auth.domain.department import Department
from app.app import db


class DepartmentDAO:

    @staticmethod
    def add_departments():
        departments_data = [
            (1, 'Lviv', '№47', '+380(65)784 54 84'),
            (2, 'Lviv', '№23', '+380(56)751 54 46'),
            (3, 'Lviv', '№71', '+380(69)654 95 12'),
            (4, 'Lviv', '№42', '+380(95)856 48 26'),
            (5, 'Lviv', '№12', '+380(65)784 12 56'),
            (6, 'Kharkiv', '№55', '+380(66)123 45 67'),
            (7, 'Odessa', '№19', '+380(67)987 65 43'),
            (8, 'Poltava', '№7', '+380(68)456 78 90'),
            (9, 'Vinnytsia', '№31', '+380(69)111 22 33'),
            (10, 'Chernihiv', '№6', '+380(67)543 21 89')
        ]

        # Додати значення в таблицю department
        for dep_id, location, number, contacts in departments_data:
            department = Department(id=dep_id, location=location, number=number, contacts=contacts)
            db.session.add(department)

        # Зберегти зміни в базі даних
        db.session.commit()

    @staticmethod
    def create_department(location, number, contacts, city_id, user_id):
        department = Department(location=location, number=number, contacts=contacts, city_id=city_id, User_id=user_id)
        db.session.add(department)
        db.session.commit()
        return department

    @staticmethod
    def get_department_by_id(department_id):
        return Department.query.get(department_id)

    @staticmethod
    def get_all_departments():
        return Department.query.all()

    @staticmethod
    def update_department(department_id, location, number, contacts, city_id, user_id):
        department = Department.query.get(department_id)
        if department:
            department.location = location
            department.number = number
            department.contacts = contacts
            department.city_id = city_id
            department.User_id = user_id
            db.session.commit()
            return department
        return None

    @staticmethod
    def delete_department(department_id):
        department = Department.query.get(department_id)
        if department:
            db.session.delete(department)
            db.session.commit()
            return department
        return None

    @staticmethod
    def init_app(app):
        db.init_app(app)
        with app.app_context():
            db.create_all()
