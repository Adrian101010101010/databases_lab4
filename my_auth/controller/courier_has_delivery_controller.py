class CourierHasDeliveryController:
    @staticmethod
    def add_courier_has_delivery(courier_id, delivery_id):
        courier_has_delivery = CourierHasDelivery(courier_id=courier_id, delivery_id=delivery_id)
        CourierHasDeliveryDAO.add_courier_has_delivery(courier_has_delivery)
        return f"Courier {courier_id} has been assigned to delivery {delivery_id}."
