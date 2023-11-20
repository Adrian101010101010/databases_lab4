class ParcelHasCourierController:
    @staticmethod
    def add_parcel_has_courier(parcel_id, courier_id):
        parcel_has_courier = ParcelHasCourier(parcel_id=parcel_id, courier_id=courier_id)
        ParcelHasCourierDAO.add_parcel_has_courier(parcel_has_courier)
        return f"Parcel {parcel_id} has been assigned to courier {courier_id}."
