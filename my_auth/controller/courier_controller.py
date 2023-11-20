from flask import jsonify, request
from ..dao.courier_dao import CourierDAO
from app.app import app

courier_dao = CourierDAO()

@app.route('/couriers', methods=['GET'])
def get_all_couriers():
    couriers = courier_dao.get_all_couriers()
    courier_list = []
    for courier in couriers:
        courier_list.append({
            'id': courier.id,
            'name': courier.name,
            'surname': courier.surname,
            'phone': courier.phone,
            'birthday': str(courier.birthday),
        })
    return jsonify({'couriers': courier_list})

@app.route('/couriers/<int:courier_id>', methods=['GET'])
def get_courier(courier_id):
    courier = courier_dao.get_courier_by_id(courier_id)
    if courier:
        return jsonify({
            'id': courier.id,
            'name': courier.name,
            'surname': courier.surname,
            'phone': courier.phone,
            'birthday': str(courier.birthday),
        })
    else:
        return jsonify({'message': 'Courier not found'}), 404

@app.route('/couriers', methods=['POST'])
def create_courier():
    data = request.get_json()
    name = data['name']
    surname = data['surname']
    phone = data['phone']
    birthday = data['birthday']
    courier = courier_dao.create_courier(name, surname, phone, birthday)
    return jsonify({
        'id': courier.id,
        'name': courier.name,
        'surname': courier.surname,
        'phone': courier.phone,
        'birthday': str(courier.birthday),
    }), 201

@app.route('/couriers/<int:courier_id>', methods=['PUT'])
def update_courier(courier_id):
    data = request.get_json()
    new_name = data['name']
    new_surname = data['surname']
    new_phone = data['phone']
    new_birthday = data['birthday']
    courier = courier_dao.update_courier(courier_id, new_name, new_surname, new_phone, new_birthday)
    if courier:
        return jsonify({
            'id': courier.id,
            'name': courier.name,
            'surname': courier.surname,
            'phone': courier.phone,
            'birthday': str(courier.birthday),
        })
    else:
        return jsonify({'message': 'Courier not found'}), 404

@app.route('/couriers/<int:courier_id>', methods=['DELETE'])
def delete_courier(courier_id):
    courier = courier_dao.delete_courier(courier_id)
    if courier:
        return jsonify({
            'id': courier.id,
            'name': courier.name,
            'surname': courier.surname,
            'phone': courier.phone,
            'birthday': str(courier.birthday),
        })
    else:
        return jsonify({'message': 'Courier not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
