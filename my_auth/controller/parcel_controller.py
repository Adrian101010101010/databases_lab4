from flask import jsonify, request
from ..dao.parcel_dao import ParcelDAO
from app.app import app

parcel_dao = ParcelDAO()

@app.route('/parcels', methods=['GET'])
def get_all_parcels():
    parcels = parcel_dao.get_all_parcels()
    parcel_list = []
    for parcel in parcels:
        parcel_list.append({
            'id': parcel.id,
            'description': parcel.description,
            'weight': parcel.weight,
            'status': parcel.status,
            'User_id': parcel.User_id,
        })
    return jsonify({'parcels': parcel_list})

@app.route('/parcels/<int:parcel_id>', methods=['GET'])
def get_parcel(parcel_id):
    parcel = parcel_dao.get_parcel_by_id(parcel_id)
    if parcel:
        return jsonify({
            'id': parcel.id,
            'description': parcel.description,
            'weight': parcel.weight,
            'status': parcel.status,
            'User_id': parcel.User_id,
        })
    else:
        return jsonify({'message': 'Parcel not found'}), 404

@app.route('/parcels', methods=['POST'])
def create_parcel():
    data = request.get_json()
    description = data['description']
    weight = data['weight']
    status = data['status']
    User_id = data['User_id']
    parcel = parcel_dao.create_parcel(description, weight, status, User_id)
    return jsonify({
        'id': parcel.id,
        'description': parcel.description,
        'weight': parcel.weight,
        'status': parcel.status,
        'User_id': parcel.User_id,
    }), 201

@app.route('/parcels/<int:parcel_id>', methods=['PUT'])
def update_parcel(parcel_id):
    data = request.get_json()
    new_description = data['description']
    new_weight = data['weight']
    new_status = data['status']
    new_User_id = data['User_id']
    parcel = parcel_dao.update_parcel(parcel_id, new_description, new_weight, new_status, new_User_id)
    if parcel:
        return jsonify({
            'id': parcel.id,
            'description': parcel.description,
            'weight': parcel.weight,
            'status': parcel.status,
            'User_id': parcel.User_id,
        })
    else:
        return jsonify({'message': 'Parcel not found'}), 404

@app.route('/parcels/<int:parcel_id>', methods=['DELETE'])
def delete_parcel(parcel_id):
    parcel = parcel_dao.delete_parcel(parcel_id)
    if parcel:
        return jsonify({
            'id': parcel.id,
            'description': parcel.description,
            'weight': parcel.weight,
            'status': parcel.status,
            'User_id': parcel.User_id,
        })
    else:
        return jsonify({'message': 'Parcel not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
