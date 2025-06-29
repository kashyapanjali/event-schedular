from flask import Flask, request, jsonify
from utils import load_events, save_events, get_next_id, sort_events
import json
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = "events.json"

# Load events from file  .. flask backend routes define
def load_events():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save events to file
def save_events(events):
    with open(DATA_FILE, "w") as f:
        json.dump(events, f, indent=4)

# Get next event ID
def get_next_id(events):
    return max([event["id"] for event in events], default=0) + 1

# Helper to sort events
def sort_events(events):
    return sorted(events, key=lambda x: datetime.strptime(x["start_time"], "%Y-%m-%d %H:%M"))

# API Routes for create, get, delete, update and search

# Create Event
@app.route("/events", methods=["POST"])
def create_event():
    data = request.json
    required_fields = ["title", "description", "start_time", "end_time"]

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        datetime.strptime(data["start_time"], "%Y-%m-%d %H:%M")
        datetime.strptime(data["end_time"], "%Y-%m-%d %H:%M")
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD HH:MM"}), 400

    events = load_events()
    new_event = {
        "id": get_next_id(events),
        "title": data["title"],
        "description": data["description"],
        "start_time": data["start_time"],
        "end_time": data["end_time"],
        "recurring": data.get("recurring")  # optional
    }
    events.append(new_event)
    save_events(events)
    return jsonify(new_event), 201


# find specific list by id  
@app.route("/events/<int:event_id>", methods=["GET"])
def get_event(event_id):
    events = load_events()
    for event in events:
        if event.get("id") == event_id:
            return jsonify(event)
    abort(404, description=f"Event with ID {event_id} not found.")


# List All Events
@app.route("/events", methods=["GET"])
def list_events():
    events = load_events()
    return jsonify(sort_events(events)), 200

# Update Event
@app.route("/events/<int:event_id>", methods=["PUT"])
def update_event(event_id):
    events = load_events()
    event = next((e for e in events if e["id"] == event_id), None)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    data = request.json
    for key in ["title", "description", "start_time", "end_time", "recurring"]:
        if key in data:
            if key in ["start_time", "end_time"]:
                try:
                    datetime.strptime(data[key], "%Y-%m-%d %H:%M")
                except ValueError:
                    return jsonify({"error": f"Invalid format for {key}. Use YYYY-MM-DD HH:MM"}), 400
            event[key] = data[key]

    save_events(events)
    return jsonify(event), 200

# Delete Event
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    events = load_events()
    updated_events = [e for e in events if e["id"] != event_id]
    if len(events) == len(updated_events):
        return jsonify({"error": "Event not found"}), 404

    save_events(updated_events)
    return jsonify({"message": "Event deleted successfully"}), 200

# Search Event
@app.route("/events/search", methods=["GET"])
def search_events():
    query = request.args.get("query", "").lower()
    events = load_events()
    results = [e for e in events if query in e["title"].lower() or query in e["description"].lower()]
    return jsonify(results), 200


if __name__ == "__main__":
    app.run(debug=True)
