from ..controller.city_controller import city_controller
from app.app import app

@app.route('/cities', methods=['GET'])
def get_all_cities():
    return city_controller.get_all_cities()

@app.route('/cities/<int:id>', methods=['GET'])
def get_city(id):
    return city_controller.get_city(id)

@app.route('/cities', methods=['POST'])
def create_city():
    return city_controller.create_city()

@app.route('/cities/<int:id>', methods=['PUT'])
def update_city(id):
    return city_controller.update_city(id)

@app.route('/cities/<int:id>', methods=['DELETE'])
def delete_city(id):
    return city_controller.delete_city(id)

if __name__ == '__main__':
    app.run(debug=True)
