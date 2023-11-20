class ParcelHasCourierDAO:
    @staticmethod
    def add_parcel_has_courier(parcel_has_courier):
        db.session.add(parcel_has_courier)
        db.session.commit()
