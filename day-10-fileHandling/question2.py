import csv
import os

FILE_NAME = 'students.csv'


def add_student():
    name = input("Enter name: ").strip().title()
    age = input("Enter age: ").strip()
    grade = input("Enter grade: ").strip()

    try:
        with open(FILE_NAME, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'Grade'])
            if file.tell() == 0:
                writer.writeheader()  
            writer.writerow({'Name': name, 'Age': age, 'Grade': grade})
        print(f"Student {name} added successfully.\n")
    except Exception as e:
        print(f"Error while adding student: {e}")


def view_students():
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.DictReader(file)
            students = list(reader)
            if not students:
                print("No student records found.")
                return
            print("\n{:<15} {:<5} {:<6}".format("Name", "Age", "Grade"))
            print("-" * 30)
            for row in students:
                print("{:<15} {:<5} {:<6}".format(row['Name'], row['Age'], row['Grade']))
    except FileNotFoundError:
        print("No records found. File does not exist.")
    except Exception as e:
        print(f"Error reading file: {e}")


def find_above_grade():
    try:
        threshold = float(input("Enter grade threshold: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.DictReader(file)
            found = False
            print("\nStudents scoring above", threshold)
            print("{:<15} {:<5} {:<6}".format("Name", "Age", "Grade"))
            print("-" * 30)
            for row in reader:
                if float(row['Grade']) > threshold:
                    print("{:<15} {:<5} {:<6}".format(row['Name'], row['Age'], row['Grade']))
                    found = True
            if not found:
                print("No students found with grade above threshold.")
    except FileNotFoundError:
        print("No records found. File does not exist.")
    except Exception as e:
        print(f"Error: {e}")

# Main program loop
def main():
    while True:
        print("\n==== Student Records Menu ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Find Students Above Grade")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            find_above_grade()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()