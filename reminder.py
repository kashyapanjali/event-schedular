import time
from datetime import datetime, timedelta
from utils import load_events, sort_events

def check_for_reminders():
    events = load_events()
    now = datetime.now()
    one_hour_later = now + timedelta(hours=1)

    upcoming = []
    for event in sort_events(events):
        start = datetime.strptime(event["start_time"], "%Y-%m-%d %H:%M")
        if now <= start <= one_hour_later:
            upcoming.append(event)

    return upcoming

def start_reminder_loop():
    print("Event Reminder System Started...\n")
    while True:
        events_due = check_for_reminders()
        if events_due:
            print(f"Reminders ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}):")
            for event in events_due:
                print(f"'{event['title']}' at {event['start_time']} - {event['description']}")
            print("-" * 50)
        time.sleep(60)  # Wait 60 seconds before checking again

if __name__ == "__main__":
    start_reminder_loop()
