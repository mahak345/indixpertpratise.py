import json  # This helps us save and load data in a file

# Function to register a student
def register_student(student, filename="students.json"):
    try:
        # Try to open the file and read existing data
        with open(filename, "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list
        students = []

    # Add the new student to the list
    students.append(student)

    # Save the updated list back to the file
    with open(filename, "w") as file:
        json.dump(students, file, indent=4)

    print("✅ Student registered successfully!")

# Function to show all students
def show_all_students(filename="students.json"):
    try:
        # Try to open and read student data
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

# Function to search students by location
def search_by_location(location, filename="students.json"):
    try:
        with open(filename, "r") as file:
            students = json.load(file)

        found = []

        for student in students:
            if student.get("location", "").lower() == location.lower():
                found.append(student)

        if found:
            print(f"📍 Students in {location}:")
            for student in found:
                print(student)
        else:
            print(f"❌ No students found in {location}.")

    except FileNotFoundError:
        print("😕 No student data found.")

# Main menu to use the program
while True:
    print("\n📚 Student Registration System")
    print("1. Register Student")
    print("2. Show All Students")
    print("3. Search Student by Location")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        # Ask user for student info
        student_id = input("Enter student ID: ")
        name = input("Enter name: ")
        contact = input("Enter contact info: ")
        location = input("Enter location: ")
        qualifications = input("Enter qualifications: ")

        # Store the data in a dictionary
        student = {
            "id": student_id,
            "name": name,
            "contact": contact,
            "location": location,
            "qualifications": qualifications
        }

        register_student(student)

    elif choice == "2":
        show_all_students()

    elif choice == "3":
        loc = input("Enter location to search: ")
        search_by_location(loc)

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please enter a number from 1 to 4.")
