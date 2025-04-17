import json

def register_student(student, filename="students.json"):
    try:
        with open(filename, "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []

    students.append(student)

    with open(filename, "w") as file:
        json.dump(students, file, indent=4)

    print("✅ Student registered successfully!")

def show_all_students(filename="students.json"):
    try:
        with open(filename, "r") as file:
            students = json.load(file)

        if not students:
            print("😕 No students registered yet.")
            return

        print("📋 List of registered students:")
        for student in students:
            print(student)

    except FileNotFoundError:
        print("😕 No student data found.")

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
