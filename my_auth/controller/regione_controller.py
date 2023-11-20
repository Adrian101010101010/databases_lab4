from flask import jsonify, request
from ..dao.regione_dao import RegioneDAO
from app.app import app

regione_dao = RegioneDAO()

@app.route('/regiones', methods=['GET'])
def get_all_regiones():
    regiones = regione_dao.get_all_regiones()
    regione_list = []
    for regione in regiones:
        regione_list.append({
            'name': regione.name,
        })
    return jsonify({'regiones': regione_list})

@app.route('/regiones/<string:name>', methods=['GET'])
def get_regione(name):
    regione = regione_dao.get_regione_by_name(name)
    if regione:
        return jsonify({
            'name': regione.name,
        })
    else:
        return jsonify({'message': 'Regione not found'}), 404

@app.route('/regiones', methods=['POST'])
def create_regione():
    data = request.get_json()
    name = data['name']
    regione = regione_dao.create_regione(name)
    return jsonify({
        'name': regione.name,
    }), 201

@app.route('/regiones/<string:name>', methods=['PUT'])
def update_regione(name):
    data = request.get_json()
    regione = regione_dao.update_regione(name)
    if regione:
        return jsonify({
            'name': regione.name,
        })
    else:
        return jsonify({'message': 'Regione not found'}), 404

@app.route('/regiones/<string:name>', methods=['DELETE'])
def delete_regione(name):
    regione = regione_dao.delete_regione(name)
    if regione:
        return jsonify({
            'name': regione.name,
        })
    else:
        return jsonify({'message': 'Regione not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
