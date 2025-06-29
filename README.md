# Event Scheduler System

A simple backend application built using Python (Flask) that allows users to create, view, update, delete, and search events with persistent storage. This project was developed as part of the Code Assessment for Biz Digital IT Services Pvt. Ltd.

---

## Tech Stack

- Python 3.x
- Flask
- REST APIs
- JSON file storage
- Postman (for testing)
- Pytest (unit testing) 
- APScheduler (reminders)

---

## Project Structure

event_scheduler/
├── app.py             # Main Flask Application  
├── events.json        # File to store event data  
├── utils.py           # Utility functions (load/save/sort)  
├── reminder.py        # Bonus: Reminders within the next hour  
├── test_app.py        # Bonus: Unit tests using Pytest  
├── requirements.txt   # Dependencies  
└── README.md          # Project Documentation  

---

## Installation Instructions

1. Clone the Repository:
   git clone https://github.com/kashyapanjali/event-schedular.git
   cd event-schedular

2. Install Required Packages:
   pip install -r requirements.txt

3. Run the Application:
   python app.py

   The server will start on: http://127.0.0.1:5000

---

## How to Test using Postman

---

## API Endpoints

1. Create Event  
Method: POST  
URL: /events  
Body:
{
  "title": "Team Meeting",
  "description": "Monthly sync-up",
  "start_time": "2025-06-29 14:00",
  "end_time": "2025-06-29 15:00"
}

2. Get All Events  
Method: GET  
URL: /events  

3. Search Events  
Method: GET  
URL: /events/search?query=meeting  

4. Update Event  
Method: PUT  
URL: /events/<id>  
Body:
{
  "title": "Updated Title"
}

5. Delete Event  
Method: DELETE  
URL: /events/<id>

---

## Bonus Features

- Reminders: Run reminder.py to check events starting within the next hour every minute.
  Command: python reminder.py

- Unit Tests: Run automated tests using Pytest.
  Command: pytest test_app.py

---

## Example cURL Request

curl -X POST http://127.0.0.1:5000/events \
  -H "Content-Type: application/json" \
  -d '{"title":"Doctor Visit","description":"Dentist","start_time":"2025-07-01 10:00","end_time":"2025-07-01 11:00"}'

---

## Author

Anjali Kashyap  
Email: anjalikashyap9608@gmail.com  
Mobile: +91-9608411997

---

## Submission Checklist

- [x] Python 3.x backend using Flask  
- [x] Events stored in events.json  
- [x] POSTMAN tested with collection exported  
- [x] README with setup, usage, and examples  
- [x] Bonus: Pytest & Reminder Feature  

---

## Notes

- Date/time format should be: YYYY-MM-DD HH:MM  
- Data is stored persistently in events.json  
- The application can be easily extended in the future

