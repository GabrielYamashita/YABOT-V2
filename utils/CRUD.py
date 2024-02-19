
import json 


def read_reminders(filePath):
    with open(filePath, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def add_reminder(filePath, reminder):
    with open(filePath, "r", encoding="utf-8") as f:
        data = json.load(f)

    data['reminders'].append(reminder)

    with open(filePath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)