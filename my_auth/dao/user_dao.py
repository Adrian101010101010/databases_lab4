from my_auth.domain.user import User
from app.app import db

class UserDAO:
    @staticmethod
    def add_users():
        users_data = [
            (1, 'Andriy', 'Kub', '+380(93)7229 63 80', '2001-12-24', 'self pickup'),
            (2, 'Igod', 'Smuk', '+380(36)943 92 00', '2002-04-15', 'self pickup'),
            (3, 'Maria', 'Petrok', '+380(75)968 62 48', '2000-07-23', 'self pickup'),
            (4, 'Ola', 'Holodnic', '+380(94)963 94 32', '2004-04-07', 'delivery'),
            (5, 'Zak', 'Kohtr', '+380(65)156 65 95', '2003-08-12', 'delivery'),
            (6, 'Vasyl', 'Koval', '+380(66)123 45 67', '2002-09-01', 'self pickup'),
            (7, 'Olha', 'Bilan', '+380(99)789 12 34', '2000-04-17', 'delivery'),
            (8, 'Ivan', 'Dovzhenko', '+380(67)456 78 90', '2001-11-25', 'self pickup'),
            (9, 'Natalia', 'Lis', '+380(63)321 54 76', '2001-01-12', 'self pickup'),
            (10, 'Taras', 'Sydor', '+380(96)876 54 32', '2002-03-04', 'delivery')
        ]

        # Додати значення в таблицю user
        for user_data in users_data:
            user = User(
                id=user_data[0],
                name=user_data[1],
                surname=user_data[2],
                phone=user_data[3],
                birthday=user_data[4],
                place_of_delivery=user_data[5]
            )
            db.session.add(user)

        # Зберегти зміни в базі даних
        db.session.commit()

    @staticmethod
    def create_user(name, surname, phone, birthday, place_of_delivery):
        user = User(name=name, surname=surname, phone=phone, birthday=birthday, place_of_delivery=place_of_delivery)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def update_user(user_id, new_name, new_surname, new_phone, new_birthday, new_place_of_delivery):
        user = User.query.get(user_id)
        if user:
            user.name = new_name
            user.surname = new_surname
            user.phone = new_phone
            user.birthday = new_birthday
            user.place_of_delivery = new_place_of_delivery
            db.session.commit()
            return user
        return None

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return user
        return None

    @staticmethod
    def init_app(app):
        db.init_app(app)
        with app.app_context():
            db.create_all()
