from flask import jsonify, request
from ..dao.delivery_dao import DeliveryDAO
from app.app import app

delivery_dao = DeliveryDAO()

@app.route('/deliveries', methods=['GET'])
def get_all_deliveries():
    deliveries = delivery_dao.get_all_deliveries()
    delivery_list = []
    for delivery in deliveries:
        delivery_list.append({
            'id': delivery.id,
            'recipient': delivery.recipient,
            'cargo_volume': delivery.cargo_volume,
            'user_id': delivery.user_id,
            # додайте інші поля за потреби
        })
    return jsonify({'deliveries': delivery_list})

@app.route('/deliveries/<int:delivery_id>', methods=['GET'])
def get_delivery(delivery_id):
    delivery = delivery_dao.get_delivery_by_id(delivery_id)
    if delivery:
        return jsonify({
            'id': delivery.id,
            'recipient': delivery.recipient,
            'cargo_volume': delivery.cargo_volume,
            'user_id': delivery.user_id,
            # додайте інші поля за потреби
        })
    else:
        return jsonify({'message': 'Delivery not found'}), 404

@app.route('/deliveries', methods=['POST'])
def create_delivery():
    data = request.get_json()
    recipient = data['recipient']
    cargo_volume = data['cargo_volume']
    user_id = data['user_id']
    # додайте інші поля за потреби
    delivery = delivery_dao.create_delivery(recipient, cargo_volume, user_id)
    return jsonify({
        'id': delivery.id,
        'recipient': delivery.recipient,
        'cargo_volume': delivery.cargo_volume,
        'user_id': delivery.user_id,
        # додайте інші поля за потреби
    }), 201

@app.route('/deliveries/<int:delivery_id>', methods=['PUT'])
def update_delivery(delivery_id):
    data = request.get_json()
    new_recipient = data['recipient']
    new_cargo_volume = data['cargo_volume']
    new_user_id = data['user_id']
    # додайте інші поля за потреби
    delivery = delivery_dao.update_delivery(delivery_id, new_recipient, new_cargo_volume, new_user_id)
    if delivery:
        return jsonify({
            'id': delivery.id,
            'recipient': delivery.recipient,
            'cargo_volume': delivery.cargo_volume,
            'user_id': delivery.user_id,
            # додайте інші поля за потреби
        })
    else:
        return jsonify({'message': 'Delivery not found'}), 404

@app.route('/deliveries/<int:delivery_id>', methods=['DELETE'])
def delete_delivery(delivery_id):
    delivery = delivery_dao.delete_delivery(delivery_id)
    if delivery:
        return jsonify({
            'id': delivery.id,
            'recipient': delivery.recipient,
            'cargo_volume': delivery.cargo_volume,
            'user_id': delivery.user_id,
            # додайте інші поля за потреби
        })
    else:
        return jsonify({'message': 'Delivery not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
