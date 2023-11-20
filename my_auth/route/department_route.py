from ..controller.department_controller import department_controller
from app.app import app

@app.route('/departments', methods=['GET'])
def get_all_departments():
    return department_controller.get_all_departments()

@app.route('/departments/<int:id>', methods=['GET'])
def get_department(id):
    return department_controller.get_department(id)

@app.route('/departments', methods=['POST'])
def create_department():
    return department_controller.create_department()

@app.route('/departments/<int:id>', methods=['PUT'])
def update_department(id):
    return department_controller.update_department(id)

@app.route('/departments/<int:id>', methods=['DELETE'])
def delete_department(id):
    return department_controller.delete_department(id)

if __name__ == '__main__':
    app.run(debug=True)
