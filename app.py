import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["student_db"]
collection = db["students"]

def add_student(name, age, grade):
    student = {"name": name, "age": age, "grade": grade}
    collection.insert_one(student)
    print("Student added successfully.")

def get_students():
    students = collection.find()
    for student in students:
        print(student)

def find_student(name):
    student = collection.find_one({"name": name})
    if student:
        print(student)
    else:
        print("Student not found.")

def delete_student(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count:
        print("Student deleted successfully.")
    else:
        print("Student not found.")

def update_student(name, new_age, new_grade):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age, "grade": new_grade}})
    if result.modified_count:
        print("Student updated successfully.")
    else:
        print("Student not found.")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Find Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            add_student(name, age, grade)
        elif choice == "2":
            get_students()
        elif choice == "3":
            name = input("Enter student name to search: ")
            find_student(name)
        elif choice == "4":
            name = input("Enter student name to delete: ")
            delete_student(name)
        elif choice == "5":
            name = input("Enter student name to update: ")
            new_age = int(input("Enter new age: "))
            new_grade = input("Enter new grade: ")
            update_student(name, new_age, new_grade)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
