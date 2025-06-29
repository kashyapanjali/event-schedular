import json
import os
from datetime import datetime

DATA_FILE = "events.json"

def load_events():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_events(events):
    with open(DATA_FILE, "w") as f:
        json.dump(events, f, indent=4)

def get_next_id(events):
    return max([event["id"] for event in events], default=0) + 1

def sort_events(events):
    return sorted(events, key=lambda x: datetime.strptime(x["start_time"], "%Y-%m-%d %H:%M"))
