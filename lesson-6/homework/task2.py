import json

file_path = r"D:\MAAB academy new\python\homework\lesson-6\homework\employees.txt"


def add_employee():
    employee = {
    'id': int(input("Enter new Employee's ID: ")),
    'name': input("Enter name: "),
    'position': input("Enter the position: "),
    'salary': int(input("Enter the salary: "))
}


    with open(file_path, 'w', encoding="utf-8") as file:
        json.dump(employee, file, indent=4)
def view_employees():
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            employees = file.readlines()  # Read all lines

        if not employees:
            print("⚠ No employee records found!")
            return
        print("\n Employee Records:")
        print("-" * 50)

        for line in employees:
            employee = json.loads(line.strip())  # Convert JSON string to dictionary
            print(f" ID: {employee['id']},  Name: {employee['name']}, Position: {employee['position']}, Salary: ${employee['salary']}")
        
    except FileNotFoundError:
        print(" Employee records file not found!")


print("1. Add new employee record \n2. View all employee records \n3. Search for an employee by Employee ID \n4. Update an employee's information \n5. Delete an employee record \n6. Exit")
print('-'*50)
print("Choose numbers from 1 to 6: ")
service=int(input())
if service==1: 
    add_employee()
    
if service==2:
    view_employees()


