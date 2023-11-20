from ..controller.user_controller import user_controller
from app.app import app

@app.route('/users', methods=['GET'])
def get_all_users():
    return user_controller.get_all_users()

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return user_controller.get_user(user_id)

@app.route('/users', methods=['POST'])
def create_user():
    return user_controller.create_user()

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return user_controller.update_user(user_id)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return user_controller.delete_user(user_id)

if __name__ == '__main__':
    app.run(debug=True)
