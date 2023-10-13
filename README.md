# Employee Database Ver 2.0

## Overview

Employee Database Ver 2.0 is a Python-based command-line application for managing employee data. This application offers two main functionalities:

1. Employee Login: Employees can log in to the system to perform operations related to their salary and personal information.

2. Admin/HRA Login: Admins or HRAs can log in to perform administrative tasks such as adding, updating, or deleting employee records.

## Features

- Employee Login:
  - Calculate Gross Salary
  - Calculate Net Salary
  - Calculate HRA (House Rent Allowance)
  - Calculate DA (Daily Allowance)

- Admin/HRA Login:
  - Upload data of a new employee
  - Check data of an employee
  - Remove data of an employee
  - Update employee details

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/msproductions/employee-database.git
   ```

2. Run the application:

   ```bash
   python Employee-Salary-Calculator-and-Employee-MGMT.py
   ```

## Usage

- When the application is launched, you will be prompted to choose between Employee Login and Admin/HRA Login. Follow the prompts to perform the desired actions.

## Database

- The application uses an SQLite database (`EmployeeDB.db`) to store employee data.

- Employee data is organized in a table named `Empl`, which includes columns for Employee ID, Password, Name, Phone, Age, Department, and Salary.

## Developer

- Lead Developer: Meit Sant

## About

This application was developed by Meit Sant and is maintained by MS Productions.
