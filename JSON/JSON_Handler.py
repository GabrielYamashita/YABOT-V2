
import json 


# Read JSON File
def read_reminders(filePath):
    with open(filePath, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


# Add Reminder inside JSON File
def add_reminder(filePath, reminder):
    with open(filePath, "r", encoding="utf-8") as f:
        data = json.load(f)

    data['reminders'].append(reminder)

    with open(filePath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


# Change State from JSON File
def change_state(filePath, setState):
    with open(filePath, "r", encoding="utf-8") as f:
        data = json.load(f)

    currState = data["state"]
    data["state"] = setState

    with open(filePath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    return currState