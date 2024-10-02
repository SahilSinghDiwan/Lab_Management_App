from flask import Flask, jsonify, request

app = Flask(__name__)

# Example route for adding inventory items
@app.route('/items', methods=['POST'])
def add_items():
    data = request.get_json()
    item = {
        "name": data["name"],
        "location": data["location"],
        "quantity": data["quantity"]
    }
    return jsonify({'message':"Item added successfully!", "item":item}), 201


# Example route for viewing all items
@app.route('/items', methods=['GET'])
def get_items():
    items = [
        {
            "name":"Breaker",
            "location":"shelf 1",
            "quantity": 10
            },
        {
            "name": "Microscope",
            "location":"Room A",
            "quantity": 1
            },        
    ]
    return jsonify(items)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5551)