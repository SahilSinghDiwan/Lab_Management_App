from flask import Flask, jsonify, request
from models.item_model import db, Item
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# # If using Flask  < 2.3
# @app.before_first_request #todo search about this function
# def create_tables():
#     db.create_all()
#
#  OR
# push context manually to app
with app.app_context():
    db.create_all()
    

# Create inventory items route
@app.route('/items', methods=['POST'])
def add_items():
    data = request.get_json()
    new_item = Item(
        name = data["name"],
        location =  data["location"],
        quantity =  data["quantity"]
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message':"Item added successfully!", "item":new_item.to_dict()}), 201


# Get all items route
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([item.json() for item in items])

# Get item by ID route
@app.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item = Item.query.get(id)
    if item:
        return jsonify(item.to_dict())
    else:
        return jsonify({'message': 'Item not found'}), 404
    
# Update item by ID route
@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.json
    item = Item.query.get(id)
    if not item:
        return jsonify({'message': 'Item not found'}), 404
    
    item.name = data.get('name', item.name)
    item.location = data.get('location', item.location)
    item.quantity = data.get('quantity', item.quantity)
    
    # Save the item
    db.session.commit() 
    
    return jsonify({'message': 'Item updated successfully', 'item': item.to_dict()})

# Delete item by ID route
@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get(id)
    if not item:
        return jsonify({'message': 'Item not found'}), 404

    db.session.delete(item)  
    db.session.commit()  

    return jsonify({'message': 'Item deleted successfully'})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5551)
    