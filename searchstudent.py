import json

def search_by_location(location, filename="students.json"):
    try:
        with open(filename, "r") as file:
            students = json.load(file)

        found = [s for s in students if s.get("location", "").lower() == location.lower()]

        if found:
            print(f"📍 Students in {location}:")
            for student in found:
                print(student)
        else:
            print(f"❌ No students found in {location}.")

    except FileNotFoundError:
        print("😕 No student data found.")
