from ..controller.courier_controller import courier_controller
from app.app import app

@app.route('/couriers', methods=['GET'])
def get_all_couriers():
    return courier_controller.get_all_couriers()

@app.route('/couriers/<int:id>', methods=['GET'])
def get_courier(id):
    return courier_controller.get_courier(id)

@app.route('/couriers', methods=['POST'])
def create_courier():
    return courier_controller.create_courier()

@app.route('/couriers/<int:id>', methods=['PUT'])
def update_courier(id):
    return courier_controller.update_courier(id)

@app.route('/couriers/<int:id>', methods=['DELETE'])
def delete_courier(id):
    return courier_controller.delete_courier(id)

if __name__ == '__main__':
    app.run(debug=True)
