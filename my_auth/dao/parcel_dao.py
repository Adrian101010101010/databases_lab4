from my_auth.domain.parcel import Parcel
from app.app import db

class ParcelDAO:
    @staticmethod
    def add_parcels():
        parcels_data = [
            (1, 'крихке', '100 KG', 'Відправляється'),
            (2, 'крихке', '5 KG', 'Відправляється'),
            (3, 'крихке', '2 KG', 'В дорозі '),
            (4, 'крихке', '1 KG', 'В точці видіці'),
            (5, 'крихке', '500 KG', 'В точці видаці'),
            (6, 'фарфорова статуетка', '3 KG', 'Відправляється'),
            (7, 'крихке', '10 KG', 'Відправляється'),
            (8, 'дитячий одяг', '2 KG', 'В дорозі'),
            (9, 'медичне обладнання', '15 KG', 'В точці видачі'),
            (10, 'крихке', '5 KG', 'В точці видачі')
        ]

        # Додати значення в таблицю parcel
        for parcel_data in parcels_data:
            parcel = Parcel(
                id=parcel_data[0],
                description=parcel_data[1],
                weight=parcel_data[2],
                status=parcel_data[3]
            )
            db.session.add(parcel)

        # Зберегти зміни в базі даних
        db.session.commit()

    @staticmethod
    def create_parcel(description, weight, status, user_id):
        parcel = Parcel(description=description, weight=weight, status=status, User_id=user_id)
        db.session.add(parcel)
        db.session.commit()
        return parcel

    @staticmethod
    def get_parcel_by_id(parcel_id):
        return Parcel.query.get(parcel_id)

    @staticmethod
    def get_all_parcels():
        return Parcel.query.all()

    @staticmethod
    def update_parcel(parcel_id, description, weight, status, user_id):
        parcel = Parcel.query.get(parcel_id)
        if parcel:
            parcel.description = description
            parcel.weight = weight
            parcel.status = status
            parcel.User_id = user_id
            db.session.commit()
            return parcel
        return None

    @staticmethod
    def delete_parcel(parcel_id):
        parcel = Parcel.query.get(parcel_id)
        if parcel:
            db.session.delete(parcel)
            db.session.commit()
            return parcel
        return None

    @staticmethod
    def init_app(app):
        db.init_app(app)
        with app.app_context():
            db.create_all()
