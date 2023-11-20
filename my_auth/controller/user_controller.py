from flask import jsonify, request
from ..dao.user_dao import UserDAO
from app.app import app

user_dao = UserDAO()

@app.route('/users', methods=['GET'])
def get_all_users():
    users = user_dao.get_all_users()
    user_list = []
    for user in users:
        user_list.append({
            'id': user.id,
            'name': user.name,
            'surname': user.surname,
            'phone': user.phone,
            'birthday': user.birthday,
            'place_of_delivery': user.place_of_delivery,
        })
    return jsonify({'users': user_list})

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = user_dao.get_user_by_id(id)
    if user:
        return jsonify({
            'id': user.id,
            'name': user.name,
            'surname': user.surname,
            'phone': user.phone,
            'birthday': user.birthday,
            'place_of_delivery': user.place_of_delivery,
        })
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data['name']
    surname = data['surname']
    phone = data['phone']
    birthday = data['birthday']
    place_of_delivery = data['place_of_delivery']
    user = user_dao.create_user(name, surname, phone, birthday, place_of_delivery)
    return jsonify({
        'id': user.id,
        'name': user.name,
        'surname': user.surname,
        'phone': user.phone,
        'birthday': user.birthday,
        'place_of_delivery': user.place_of_delivery,
    }), 201

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = user_dao.update_user(id)
    if user:
        return jsonify({
            'id': user.id,
            'name': user.name,
            'surname': user.surname,
            'phone': user.phone,
            'birthday': user.birthday,
            'place_of_delivery': user.place_of_delivery,
        })
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = user_dao.delete_user(id)
    if user:
        return jsonify({
            'id': user.id,
            'name': user.name,
            'surname': user.surname,
            'phone': user.phone,
            'birthday': user.birthday,
            'place_of_delivery': user.place_of_delivery,
        })
    else:
        return jsonify({'message': 'User not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
