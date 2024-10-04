import os
from flask import Flask, jsonify, request , render_template
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS  # Import CORS

app = Flask(__name__)

# Enable CORS
CORS(app)

# Get MongoDB URI from environment variable
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/ticket_system')
client = MongoClient(MONGO_URI)
db = client['ticket_system']
tickets_collection = db['tickets']



@app.route('/tickets', methods=['GET'])

def get_tickets():
    tickets = list(tickets_collection.find())
    # Convert ObjectId to string for JSON serialization
    for ticket in tickets:
        ticket['_id'] = str(ticket['_id'])
    return jsonify(tickets), 200

# Route to create a new ticket
@app.route('/tickets', methods=['POST'])
def create_ticket():
    new_ticket = request.json
    new_ticket["status"] = "Nouveau"  # Set initial status
    result = tickets_collection.insert_one(new_ticket)
    new_ticket["_id"] = str(result.inserted_id)
    return jsonify(new_ticket), 201

# Route to update ticket status
@app.route('/tickets/<ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    data = request.json
    status = data.get('status')

    result = tickets_collection.update_one(
        {"_id": ObjectId(ticket_id)},
        {"$set": {"status": status}}
    )
    if result.matched_count:
        return jsonify({"message": "Ticket updated"}), 200
    else:
        return jsonify({"message": "Ticket not found"}), 404

# Route to close a ticket (status: Fermé)
@app.route('/tickets/<ticket_id>/close', methods=['PUT'])
def close_ticket(ticket_id):
    result = tickets_collection.update_one(
        {"_id": ObjectId(ticket_id)},
        {"$set": {"status": "Fermé"}}
    )
    if result.matched_count:
        return jsonify({"message": "Ticket closed"}), 200
    else:
        return jsonify({"message": "Ticket not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
