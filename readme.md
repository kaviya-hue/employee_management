# Employee Management System

A simple Python-based Employee Management System that allows users to add, view, search, and update employee information.

## Features

* Add employee details
* View all employees
* Search for an employee
* Update employee details
* Store employee information using Python dictionaries
* Simple menu-driven interface

## Technologies Used

* Python
* Dictionaries
* Functions
* Loops
* Conditional Statements
* User Input

## Installation

Make sure Python is installed on your computer.

Check the Python version:

```bash
python --version
```

## Run the Application

Run the Python file:

```bash
python main.py
```

## Example

```text
===== EMPLOYEE MANAGEMENT SYSTEM =====

1. Add Employee
2. Display Employees
3. Update Employee
4. Search Employee
5. Exit

Enter choice: 1

Enter how many data: 2

Enter ID: 101
Enter Name: Kaviya
Enter Salary: 30000

Enter ID: 102
Enter Name: Rahul
Enter Salary: 35000

Employee details added successfully!
```

## Algorithm

1. Initialize an empty dictionary to store employee records.
2. Display the Employee Management System menu.
3. Accept the user's choice.
4. If **Add Employee** is selected:

   * Enter the number of employees.
   * Accept the employee ID, name, and salary.
   * Store the details in the dictionary using the employee ID as the key.
5. If **Display Employees** is selected:

   * Display all employee records stored in the dictionary.
6. If **Update Employee** is selected:

   * Enter the employee ID.
   * Check whether the ID exists.
   * If found, update the employee's name and salary.
   * Otherwise, display "ID not found".
7. If **Search Employee** is selected:

   * Enter the employee ID.
   * Display the employee details if the ID exists.
   * Otherwise, display "NOT FOUND".
8. If **Exit** is selected:

   * Display the exit message.
   * Terminate the program.
9. Repeat the process until the user selects Exit.

## Project Structure

```text
employee-management-system/
│
├── main.py
├── README.md
└── requirements.txt
```

## Requirements

This project uses only Python's built-in features, so no external packages are required.

## Author

Kaviya
