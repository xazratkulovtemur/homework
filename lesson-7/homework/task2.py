import os 

filename = r"D:\MAAB academy new\python\homework\lesson-7\homework\employee.txt"

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class Employee_Manager:
    def __init__(self, filename):
        self.filename = filename

    def add_employee(self):
        """Adding new employee"""
        employee_id = input("Enter ID for new employee: ")

        if self.search_emp_by_id(employee_id, silent=True):
            print("The employee with this ID already exists.")
            return

        name = input("Enter name for new employee: ")
        position = input("Enter position for new employee: ")
        salary = input("Enter salary for new employee: ")

        with open(self.filename, 'a') as file:
            file.write(f"{employee_id}, {name}, {position}, {salary}\n")

        print("Employee added successfully!")

    def view_all_employees(self):
        """View all employees"""
        if not os.path.exists(self.filename):
            print("No file found!")
            return

        with open(self.filename, 'r') as file:
            employees = [line.strip().split(", ") for line in file]

        if not employees:
            print("No employees added yet!")
            return

        print("\nSort by: \n1. Name\n2. Salary")
        choice_for_sorting = input("Enter 1 or 2: ")

        if choice_for_sorting == "1":
            employees.sort(key=lambda x: x[1])
        elif choice_for_sorting == "2":
            employees.sort(key=lambda x: float(x[3]), reverse=True)

        print("\nEmployee Records:")
        for emp in employees:
            print(", ".join(emp))

    def search_emp_by_id(self, employee_id, silent=False):
        """Search employee by ID"""
        if not os.path.exists(self.filename):
            if not silent:
                print("No file found!")
            return False

        with open(self.filename, 'r') as file:
            for line in file:
                data = line.strip().split(", ")
                if data[0] == employee_id:
                    if not silent:
                        print("\nEmployee found:")
                        print(line.strip())
                    return True
        
        if not silent:
            print("No employee found with this ID.")
        return False

    def update_employee(self):
        """Updating employee information"""
        if not os.path.exists(self.filename):
            print("No file found!")
            return

        employee_id = input("Enter employee ID: ")
        employees = []

        found = False
        with open(self.filename, 'r') as file:
            for line in file:
                data = line.strip().split(", ")
                if data[0] == employee_id:
                    found = True
                    print(f"Employee found: {line.strip()}")
                    new_name = input("Enter new name: ")
                    new_position = input("Enter new position: ")
                    new_salary = input("Enter new salary: ")
                    employees.append(f"{employee_id}, {new_name}, {new_position}, {new_salary}\n")
                else:
                    employees.append(line)

        if found:
            with open(self.filename, 'w') as file:
                file.writelines(employees)
            print("Employee updated successfully!")
        else:
            print("Employee not found.")

    def delete_employee(self):
        """Deleting an employee by ID"""
        if not os.path.exists(self.filename):
            print("No file found!")
            return

        employee_id = input("Enter employee ID: ")
        employees = []
        found = False

        with open(self.filename, 'r') as file:
            for line in file:
                data = line.strip().split(", ")
                if data[0] == employee_id:
                    found = True
                    print("Employee found and will be deleted.")
                else:
                    employees.append(line)

        if found:
            with open(self.filename, 'w') as file:
                file.writelines(employees)
            print("Employee deleted successfully!")
        else:
            print("Employee not found!")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            try:
                choice = int(input("Choose (1-6): "))
                if choice == 1:
                    self.add_employee()
                elif choice == 2:
                    self.view_all_employees()
                elif choice == 3:
                    employee_id = input("Enter the ID of the employee: ")
                    self.search_emp_by_id(employee_id)
                elif choice == 4:
                    self.update_employee()
                elif choice == 5:
                    self.delete_employee()
                elif choice == 6:
                    self.exit_prog()
                    break
                else:
                    print("Please enter a number between 1 and 6!")
            except ValueError:
                print("Invalid input. Please enter a number!")

    def exit_prog(self):
        print("Program closed!")


if __name__ == "__main__":
    manager = Employee_Manager(filename)
    manager.menu()
