
class DepartmentDTO:
    def __init__(self, id, location, number, contacts):
        self.id = id
        self.location = location
        self.number = number
        self.contacts = contacts

class CityDTO:
    def __init__(self, id, city_name):
        self.id = id
        self.city_name = city_name

class RegioneDTO:
    def __init__(self, name):
        self.name = name

class UserDTO:
    def __init__(self, id, name, surname, phone, birthday, place_of_delivery):
        self.id = id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.birthday = birthday
        self.place_of_delivery = place_of_delivery

class ParcelDTO:
    def __init__(self, id, description, weight, status):
        self.id = id
        self.description = description
        self.weight = weight
        self.status = status

class OperatorDTO:
    def __init__(self, id, name, surname, phone):
        self.id = id
        self.name = name
        self.surname = surname
        self.phone = phone

class DeliveryDTO:
    def __init__(self, id, recipient, cargo_volume):
        self.id = id
        self.recipient = recipient
        self.cargo_volume = cargo_volume

class CourierDTO:
    def __init__(self, id, name, surname, phone, birthday):
        self.id = id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.birthday = birthday

class CourierHasDeliveryDTO:
    def __init__(self, courier_id, delivery_id):
        self.courier_id = courier_id
        self.delivery_id = delivery_id

class ParcelHasCourierDTO:
    def __init__(self, courier_id, parcel_id):
        self.courier_id = courier_id
        self.parcel_id = parcel_id

