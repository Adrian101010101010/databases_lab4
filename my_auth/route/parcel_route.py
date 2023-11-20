from ..controller.parcel_controller import parcel_controller
from app.app import app

@app.route('/parcels', methods=['GET'])
def get_all_parcels():
    return parcel_controller.get_all_parcels()

@app.route('/parcels/<int:id>', methods=['GET'])
def get_parcel(id):
    return parcel_controller.get_parcel(id)

@app.route('/parcels', methods=['POST'])
def create_parcel():
    return parcel_controller.create_parcel()

@app.route('/parcels/<int:id>', methods=['PUT'])
def update_parcel(id):
    return parcel_controller.update_parcel(id)

@app.route('/parcels/<int:id>', methods=['DELETE'])
def delete_parcel(id):
    return parcel_controller.delete_parcel(id)

if __name__ == '__main__':
    app.run(debug=True)
