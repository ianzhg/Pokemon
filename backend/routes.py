from flask import request, jsonify
from app import app, collection


@app.route("/")
def index():
    return "Hello world"

# Define route to store data in MongoDB
@app.route("/store_data", methods=["POST"])
def store_data():
    data = request.get_json()

    # Insert data into MongoDB with unique_id as the document _id
    result = collection.update_one({"_id": data["unique_id"]}, {"$set": data}, upsert=True)

    # Return response
    return jsonify({"message": "Data stored successfully!", "id": data["unique_id"]})

# Define route to get data from MongoDB by unique_id
@app.route("/get_data/<unique_id>", methods=["GET"])
def get_data(unique_id):
    # Find data in MongoDB by unique_id
    result = collection.find_one({"_id": unique_id})

    if result:
        # Return data if found
        return jsonify({"message": "Data retrieved successfully!", "output": result})
    else:
        # Return error message if not found
        return jsonify({"error": f"No data found for unique_id {unique_id}."})

# Define route to update data in MongoDB by unique_id. This automatically check how many fields to update and update in database
@app.route("/update_data/<unique_id>", methods=["PUT"])
def update_data(unique_id):
    data = request.get_json()

    fields_to_update = {}
    for field, value in data.items():
        if field == "JP_price":
            fields_to_update["JP_price"] = value
        elif field == "JP_name":
            fields_to_update["JP_name"] = value
        elif field == "US_name":
            fields_to_update["US_name"] = value
        elif field == "US_price":
            fields_to_update["US_price"] = value

    if fields_to_update:
        # Update data in MongoDB by unique_id
        result = collection.update_one({"_id": unique_id}, {"$set": fields_to_update})

        if result.modified_count > 0:
            # Return success message if at least one field was updated
            return jsonify({"message": "Data updated successfully!", "id": unique_id})
        else:
            # Return error message if no fields were updated
            return jsonify({"error": f"No fields were updated for unique_id {unique_id}."})
    else:
        # Return error message if no fields were present in the input
        return jsonify({"error": "No fields present in input."})