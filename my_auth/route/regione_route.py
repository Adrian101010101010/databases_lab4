from ..controller.regione_controller import regione_controller
from app.app import app

@app.route('/regioni', methods=['GET'])
def get_all_regioni():
    return regione_controller.get_all_regioni()

@app.route('/regioni/<string:name>', methods=['GET'])
def get_regione(name):
    return regione_controller.get_regione(name)

@app.route('/regioni', methods=['POST'])
def create_regione():
    return regione_controller.create_regione()

@app.route('/regioni/<string:name>', methods=['PUT'])
def update_regione(name):
    return regione_controller.update_regione(name)

@app.route('/regioni/<string:name>', methods=['DELETE'])
def delete_regione(name):
    return regione_controller.delete_regione(name)

if __name__ == '__main__':
    app.run(debug=True)
