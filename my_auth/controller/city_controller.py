from flask import jsonify, request
from ..dao.city_dao import CityDAO
from app.app import app

city_dao = CityDAO()

@app.route('/cities', methods=['GET'])
def get_all_cities():
    cities = city_dao.get_all_cities()
    city_list = []
    for city in cities:
        city_list.append({
            'id': city.id,
            'city_name': city.city_name,
            'regione_name': city.regione_name,
        })
    return jsonify({'cities': city_list})

@app.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    city = city_dao.get_city_by_id(city_id)
    if city:
        return jsonify({
            'id': city.id,
            'city_name': city.city_name,
            'regione_name': city.regione_name,
        })
    else:
        return jsonify({'message': 'City not found'}), 404

@app.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    city_name = data['city_name']
    regione_name = data['regione_name']
    city = city_dao.create_city(city_name, regione_name)
    return jsonify({
        'id': city.id,
        'city_name': city.city_name,
        'regione_name': city.regione_name,
    }), 201

@app.route('/cities/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    data = request.get_json()
    new_city_name = data['city_name']
    new_regione_name = data['regione_name']
    city = city_dao.update_city(city_id, new_city_name, new_regione_name)
    if city:
        return jsonify({
            'id': city.id,
            'city_name': city.city_name,
            'regione_name': city.regione_name,
        })
    else:
        return jsonify({'message': 'City not found'}), 404

@app.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = city_dao.delete_city(city_id)
    if city:
        return jsonify({
            'id': city.id,
            'city_name': city.city_name,
            'regione_name': city.regione_name,
        })
    else:
        return jsonify({'message': 'City not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
