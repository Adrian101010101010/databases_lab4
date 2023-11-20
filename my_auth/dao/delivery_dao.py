from my_auth.domain.delivery import Delivery


class DeliveryDAO:
    @staticmethod
    def add_deliveries():
        deliveries_data = [
            (1, 'Andriy', '40*70*30'),
            (2, 'Artur', '16*72*19'),
            (3, 'Zak', '12*12*12'),
            (4, 'Dgon', '50*75*30'),
            (5, 'Dgon', '90*56*50'),
            (6, 'Mykhailo', '35*60*25'),
            (7, 'Oksana', '20*50*15'),
            (8, 'Vasyl', '42*68*33'),
            (9, 'Natalia', '28*55*20'),
            (10, 'Vitaly', '60*80*40')
        ]

        # Додати значення в таблицю delivery
        for delivery_data in deliveries_data:
            delivery = Delivery(
                id=delivery_data[0],
                recipient=delivery_data[1],
                cargo_volume=delivery_data[2]
            )
            db.session.add(delivery)

        # Зберегти зміни в базі даних
        db.session.commit()

    @staticmethod
    def create_delivery(recipient, cargo_volume, user_id):
        delivery = Delivery(recipient=recipient, cargo_volume=cargo_volume, User_id=user_id)
        db.session.add(delivery)
        db.session.commit()
        return delivery

    @staticmethod
    def get_delivery_by_id(delivery_id):
        return Delivery.query.get(delivery_id)

    @staticmethod
    def get_all_deliveries():
        return Delivery.query.all()

    @staticmethod
    def update_delivery(delivery_id, recipient, cargo_volume, user_id):
        delivery = Delivery.query.get(delivery_id)
        if delivery:
            delivery.recipient = recipient
            delivery.cargo_volume = cargo_volume
            delivery.User_id = user_id
            db.session.commit()
            return delivery
        return None

    @staticmethod
    def delete_delivery(delivery_id):
        delivery = Delivery.query.get(delivery_id)
        if delivery:
            db.session.delete(delivery)
            db.session.commit()
            return delivery
        return None

    @staticmethod
    def init_app(app):
        db.init_app(app)
        with app.app_context():
            db.create_all()


from app.app import db
