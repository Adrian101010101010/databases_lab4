class CourierHasDeliveryDAO:
    @staticmethod
    def add_courier_has_delivery(courier_has_delivery):
        db.session.add(courier_has_delivery)
        db.session.commit()