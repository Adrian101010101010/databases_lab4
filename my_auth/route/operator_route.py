from ..controller.operator_controller import operator_controller
from app.app import app

@app.route('/operators', methods=['GET'])
def get_all_operators():
    return operator_controller.get_all_operators()

@app.route('/operators/<int:id>', methods=['GET'])
def get_operator(id):
    return operator_controller.get_operator(id)

@app.route('/operators', methods=['POST'])
def create_operator():
    return operator_controller.create_operator()

@app.route('/operators/<int:id>', methods=['PUT'])
def update_operator(id):
    return operator_controller.update_operator(id)

@app.route('/operators/<int:id>', methods=['DELETE'])
def delete_operator(id):
    return operator_controller.delete_operator(id)

if __name__ == '__main__':
    app.run(debug=True)
