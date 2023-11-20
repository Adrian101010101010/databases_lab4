from ..controller.delivery_controller import delivery_controller
from app.app import app

@app.route('/deliveries', methods=['GET'])
def get_all_deliveries():
    return delivery_controller.get_all_deliveries()

@app.route('/deliveries/<int:id>', methods=['GET'])
def get_delivery(id):
    return delivery_controller.get_delivery(id)

@app.route('/deliveries', methods=['POST'])
def create_delivery():
    return delivery_controller.create_delivery()

@app.route('/deliveries/<int:id>', methods=['PUT'])
def update_delivery(id):
    return delivery_controller.update_delivery(id)

@app.route('/deliveries/<int:id>', methods=['DELETE'])
def delete_delivery(id):
    return delivery_controller.delete_delivery(id)

if __name__ == '__main__':
    app.run(debug=True)
