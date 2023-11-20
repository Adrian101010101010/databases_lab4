from flask import jsonify, request
from ..dao.department_dao import DepartmentDAO
from app.app import app

department_dao = DepartmentDAO()

@app.route('/departments', methods=['GET'])
def get_all_departments():
    departments = department_dao.get_all_departments()
    department_list = []
    for department in departments:
        department_list.append({
            'id': department.id,
            'location': department.location,
            'number': department.number,
            'contacts': department.contacts,
            'city_id': department.city_id,
            'user_id': department.user_id,
            # додайте інші поля за потреби
        })
    return jsonify({'departments': department_list})

@app.route('/departments/<int:department_id>', methods=['GET'])
def get_department(department_id):
    department = department_dao.get_department_by_id(department_id)
    if department:
        return jsonify({
            'id': department.id,
            'location': department.location,
            'number': department.number,
            'contacts': department.contacts,
            'city_id': department.city_id,
            'user_id': department.user_id,
            # додайте інші поля за потреби
        })
    else:
        return jsonify({'message': 'Department not found'}), 404

@app.route('/departments', methods=['POST'])
def create_department():
    data = request.get_json()
    location = data['location']
    number = data['number']
    contacts = data['contacts']
    city_id = data['city_id']
    user_id = data['user_id']
    # додайте інші поля за потреби
    department = department_dao.create_department(location, number, contacts, city_id, user_id)
    return jsonify({
        'id': department.id,
        'location': department.location,
        'number': department.number,
        'contacts': department.contacts,
        'city_id': department.city_id,
        'user_id': department.user_id,
        # додайте інші поля за потреби
    }), 201

@app.route('/departments/<int:department_id>', methods=['PUT'])
def update_department(department_id):
    data = request.get_json()
    new_location = data['location']
    new_number = data['number']
    new_contacts = data['contacts']
    new_city_id = data['city_id']
    new_user_id = data['user_id']
    # додайте інші поля за потреби
    department = department_dao.update_department(department_id, new_location, new_number, new_contacts, new_city_id, new_user_id)
    if department:
        return jsonify({
            'id': department.id,
            'location': department.location,
            'number': department.number,
            'contacts': department.contacts,
            'city_id': department.city_id,
            'user_id': department.user_id,
            # додайте інші поля за потреби
        })
    else:
        return jsonify({'message': 'Department not found'}), 404

@app.route('/departments/<int:department_id>', methods=['DELETE'])
def delete_department(department_id):
    department = department_dao.delete_department(department_id)
    if department:
        return jsonify({
            'id': department.id,
            'location': department.location,
            'number': department.number,
            'contacts': department.contacts,
            'city_id': department.city_id,
            'user_id': department.user_id,
            # додайте інші поля за потреби
        })
    else:
        return jsonify({'message': 'Department not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
