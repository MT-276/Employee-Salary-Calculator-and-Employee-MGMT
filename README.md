# Employee Database Ver 1.0

## Introduction
Welcome to the Employee Database Ver 1.0, a simple Python program designed for managing employee data in a database. This program allows you to perform various operations, such as uploading data for a new employee, checking the data of an existing employee, and removing data of an employee.

## Features
- **Upload Data of a New Employee**: You can input details for a new employee, such as name, phone number, age, department, and salary, and the program will save this information to the database. It will also automatically generate a unique Employee ID for the new entry.

- **Check Data of an Employee**: If you want to retrieve information about a specific employee, you can input their Employee ID, and the program will display their details, including name, phone number, age, department, and salary.

- **Remove Data of an Employee**: To delete an employee's data from the database, you can provide their Employee ID, and the program will remove their information from the database.

## Getting Started
To use this program, please follow these steps:

1. Clone or download the repository to your local machine.

2. Ensure you have Python installed, as this program is written in Python.

3. Run the program by executing the "Employee-Salary-Calculator-and-Employee-MGMT" file.

4. Follow the on-screen prompts and select the desired option (1 for uploading data, 2 for checking data, 3 for removing data).

5. For each option, follow the specific instructions provided by the program.

6. The program will interact with the database ("EmployeeDB.db") to manage employee data.

## Database Structure
The program uses an SQLite database with the following structure:
- `Emp_ID` (Employee ID): A unique identifier for each employee.
- `Emp_Name` (Employee Name): The name of the employee.
- `Emp_Phone` (Employee Phone): The phone number of the employee.
- `Emp_Age` (Employee Age): The age of the employee.
- `Emp_Dept` (Employee Department): The department to which the employee belongs.
- `Emp_Salary` (Employee Salary): The salary of the employee.

## Dependencies
The program uses Python's built-in libraries and does not require any external dependencies.

## Contributors
- Lead Developer: Meit Sant
- Organization: MS Productions


## Version History
- Version 1.0 (13th October 2023): Initial release.

Thank you for using the Employee Database Ver 1.0. We hope it helps you efficiently manage employee data.
