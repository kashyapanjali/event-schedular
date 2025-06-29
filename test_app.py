import pytest
from app import app
import json
import os

TEST_EVENTS_FILE = "events.json"

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    # Clear events before each test
    with open(TEST_EVENTS_FILE, "w") as f:
        json.dump([], f)

    yield client

# Tests 

def test_create_event(client):
    response = client.post("/events", json={
        "title": "Test Event",
        "description": "Testing create",
        "start_time": "2025-06-30 10:00",
        "end_time": "2025-06-30 11:00"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Test Event"

def test_list_events(client):
    # Add one event first
    client.post("/events", json={
        "title": "List Event",
        "description": "Testing list",
        "start_time": "2025-06-30 12:00",
        "end_time": "2025-06-30 13:00"
    })
    response = client.get("/events")
    assert response.status_code == 200
    assert len(response.get_json()) >= 1

def test_update_event(client):
    post_resp = client.post("/events", json={
        "title": "Update Me",
        "description": "Old",
        "start_time": "2025-06-30 14:00",
        "end_time": "2025-06-30 15:00"
    })
    event_id = post_resp.get_json()["id"]

    response = client.put(f"/events/{event_id}", json={
        "title": "Updated Title"
    })
    assert response.status_code == 200
    assert response.get_json()["title"] == "Updated Title"

def test_delete_event(client):
    post_resp = client.post("/events", json={
        "title": "To Delete",
        "description": "Delete this",
        "start_time": "2025-06-30 16:00",
        "end_time": "2025-06-30 17:00"
    })
    event_id = post_resp.get_json()["id"]

    response = client.delete(f"/events/{event_id}")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Event deleted successfully"

def test_search_event(client):
    client.post("/events", json={
        "title": "Searchable",
        "description": "Find me here",
        "start_time": "2025-07-01 09:00",
        "end_time": "2025-07-01 10:00"
    })

    response = client.get("/events/search?query=searchable")
    assert response.status_code == 200
    assert len(response.get_json()) > 0
