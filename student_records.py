import json

# 1. Store student details using dictionary
student_records = {
    101: {
        "name" : "Amit", 
        "age" : 20, 
        "course" : "Civil Engineering",
        "grade" : "A"
    },
    102: {
        "name" : "Neha",
        "age" : 21, 
        "course" : "Computer Science",
        "grade" : "B"
    },
    103: {
        "name" : "Rahul", 
        "age" : 19,
        "course" : "Mechanical Engineering",
        "grade" : "A+"
    }
}

print("Initial Student Records:")
print(student_records)
print("_" * 40)

# 2. Access keys and values
print("Student IDs:", student_records.keys())
print("Student Details:", student_records.values())
print("_" * 40)

# 3. Update an entry
student_records[102]["grade"] = "A"
print("Update Neha's grade")
print("_" * 40)

# 4. Delete an entry 
del student_records[101]
print("Delete record for student ID 101")
print("_" * 40)

# 5. Loop through dictionary
print("Student Records:")
for student_id, details in student_records.items():
    print(f"ID: {student_id}")
    for key, value in details.items():
        print(f"  {key.capitalize()}: {value}")
    print()

# 6. Convert dictionary to JSON and save to file 
with open("students.json", "w") as file:
    json.dump(student_records, file, indent=4)

print("Student records saved to students.json")
print("_" * 40)

# 7. Read JSON back into Python
with open("students.json", "r") as file:
    loaded_data = json.load(file)

# 8. Print clean formatted output
print("Data loaded from JSON file:")
for student_id, details in loaded_data.items():
    print(f"ID: {student_id}")
    for key, value in details.items():
        print(f"  {key.capitalize()}: {value}")
    print()