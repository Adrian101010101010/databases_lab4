from flask import jsonify, request
from ..dao.operator_dao import OperatorDAO
from app.app import app

operator_dao = OperatorDAO()

@app.route('/operators', methods=['GET'])
def get_all_operators():
    operators = operator_dao.get_all_operators()
    operator_list = []
    for operator in operators:
        operator_list.append({
            'id': operator.id,
            'name': operator.name,
            'surname': operator.surname,
            'phone': operator.phone,
            'parcel_id': operator.parcel_id,
        })
    return jsonify({'operators': operator_list})

@app.route('/operators/<int:operator_id>', methods=['GET'])
def get_operator(operator_id):
    operator = operator_dao.get_operator_by_id(operator_id)
    if operator:
        return jsonify({
            'id': operator.id,
            'name': operator.name,
            'surname': operator.surname,
            'phone': operator.phone,
            'parcel_id': operator.parcel_id,
        })
    else:
        return jsonify({'message': 'Operator not found'}), 404

@app.route('/operators', methods=['POST'])
def create_operator():
    data = request.get_json()
    name = data['name']
    surname = data['surname']
    phone = data['phone']
    parcel_id = data['parcel_id']
    operator = operator_dao.create_operator(name, surname, phone, parcel_id)
    return jsonify({
        'id': operator.id,
        'name': operator.name,
        'surname': operator.surname,
        'phone': operator.phone,
        'parcel_id': operator.parcel_id,
    }), 201

@app.route('/operators/<int:operator_id>', methods=['PUT'])
def update_operator(operator_id):
    data = request.get_json()
    new_name = data['name']
    new_surname = data['surname']
    new_phone = data['phone']
    new_parcel_id = data['parcel_id']
    operator = operator_dao.update_operator(operator_id, new_name, new_surname, new_phone, new_parcel_id)
    if operator:
        return jsonify({
            'id': operator.id,
            'name': operator.name,
            'surname': operator.surname,
            'phone': operator.phone,
            'parcel_id': operator.parcel_id,
        })
    else:
        return jsonify({'message': 'Operator not found'}), 404

@app.route('/operators/<int:operator_id>', methods=['DELETE'])
def delete_operator(operator_id):
    operator = operator_dao.delete_operator(operator_id)
    if operator:
        return jsonify({
            'id': operator.id,
            'name': operator.name,
            'surname': operator.surname,
            'phone': operator.phone,
            'parcel_id': operator.parcel_id,
        })
    else:
        return jsonify({'message': 'Operator not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
