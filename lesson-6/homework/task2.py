import os

path = "D:\MAAB academy new\python\homework\lesson-6\homework\employees.txt"  # File name

def add_employee():
    """Append a new employee record to the file."""
    with open(path, 'a') as file:
        id = input("Enter employee's ID: ")
        name = input("Enter employee's name: ")
        position = input("Enter employee's position: ")
        salary = input("Enter employee's salary: ")

        if not salary.isdigit():
            print("Invalid salary. Please enter a numeric value.")
            return
        
        file.write(f"{id}, {name}, {position}, {salary}\n")
    print("Employee added successfully!")

def view():
    """Display all employee records."""
    try:
        with open(path, 'r') as file:
            content = file.readlines()

        if not content:
            print("No employee records found.")
            return

        print("\nHere are the employees' records:\n")
        print('-' * 50)
        for line in content:
            print(line.strip())
        print('-' * 50)

    except FileNotFoundError:
        print("File not found. Please add records first.")

def search_employee(with_id):
    """Search for an employee by ID."""
    try:
        with open(path, 'r') as file:
            for line in file:
                employee_list = [word.strip() for word in line.split(',')]
                emp_id = employee_list[0]  # Keep as string to avoid int conversion issues
                if emp_id == with_id:
                    return line.strip()  # Return the employee details

        return None  # If not found, return None

    except FileNotFoundError:
        print("File not found. Please add records first.")
        return None

def update_employee():
    """Update an employee's details by ID."""
    with_id = input("Enter employee ID to update: ")
    employee = search_employee(with_id)

    if not employee:
        print("No such employee found.")
        return

    new_name = input("Enter new name: ")
    new_position = input("Enter new position: ")
    new_salary = input("Enter new salary: ")

    if not new_salary.isdigit():
        print("Invalid salary. Please enter a numeric value.")
        return

    with open(path, 'r') as file:
        lines = file.readlines()

    with open(path, 'w') as file:
        for line in lines:
            if line.startswith(with_id + ","):
                file.write(f"{with_id}, {new_name}, {new_position}, {new_salary}\n")
            else:
                file.write(line)

    print("Employee updated successfully!")

def delete_employee():
    """Delete an employee by ID."""
    with_id = input("Enter employee ID to delete: ")
    employee = search_employee(with_id)

    if not employee:
        print("No such employee found.")
        return

    with open(path, 'r') as file:
        lines = file.readlines()

    with open(path, 'w') as file:
        for line in lines:
            if not line.startswith(with_id + ","):
                file.write(line)

    print(f"Employee with ID {with_id} deleted successfully!")

def main():
    """Display menu and handle user input."""
    while True:
        print("\nEmployee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view()
        elif choice == '3':
            emp_id = input("Enter Employee ID to search: ")
            result = search_employee(emp_id)
            if result:
                print("\nEmployee found:\n", result)
            else:
                print("\nNo such employee found.")
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
