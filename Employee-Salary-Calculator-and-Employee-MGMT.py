#-------------------------------------------------------------------------------
# Name:        Employee Database Ver 2.0
#
# Created:     13 10 2023
#
# Lead Dev:    Meit Sant
# Copyright:   (c) MS Productions
#
#-------------------------------------------------------------------------------

from sys import exit
from sqlite3 import connect

option = input(
"""
Welcome to Employee management system !

Please Choose your option :
    (1) Employee Login
    (2) Admin/ HRA Login

--> """
)


# Attempting connection to database and creating table if not exists
print('\n[INFO] Initializing database')
try:
    connector = connect('EmployeeDB.db')
    connector.execute("""CREATE TABLE IF NOT EXISTS Empl(
Emp_ID  varchar(5) PRIMARY KEY,
Emp_Pwd varchar(30) NOT NULL,
Emp_Name varchar(30) NOT NULL,
Emp_Phone int(10) NOT NULL,
Emp_Age int(2) NOT NULL,
Emp_Dept varchar(30) NOT NULL,
Emp_Salary float(10) NOT NULL
);""")
    connector.commit()
    print('\n[INFO] Database connected')
except:
    print('\n[ERROR] Connection to the database failed.')
    connector.close()
    exit()


if option == '1':
    emp_id = input('\nPlease enter employee ID\n--> ')
    emp_pwd = input('\nPlease enter employee Password\n--> ')

    query = connector.execute(f'SELECT Emp_Pwd FROM Empl WHERE Emp_ID = "{emp_id}"')
    pwd = query.fetchall()
    print(pwd)
    if pwd == []:
        print(f"\n[ERROR] No employee with ID '{emp_id}' found. Please try again.")
        connector.close()
        exit()
    if emp_pwd != pwd[0][0]:
        print(f"\n[ERROR] Wrong Password. Please try again.")
        connector.close()
        exit()
    print('\n[INFO] Login success\n')
    option = input(
"""
Please Choose your option :
    1. Calculate Gross salary
    2. Calculate Net salary
    3. Calculate HRA
    4. Calculate DA

--> """
        )

    # Fetching basic salary from db
    query = connector.execute(f'SELECT Emp_Salary FROM Empl WHERE Emp_ID ="{emp_id}"')
    basic_Salary = float(query.fetchall()[0][0])

    if option == '1':
        # Gross Salary

        HRA = float(input('\nPlease enter rent paid (In ₹)\n--> ')) - (0.1*basic_Salary)
        other_Allowances = float(input('\nPlease enter Other Allowances (In ₹)\n--> '))

        gross_Salary = basic_Salary+HRA+other_Allowances

        print(f'\nGross Salary :- {gross_Salary} ')
        connector.close()
        exit()
    if option == '2':
        # Net Salary

        # HRA = Rent - 10% of basic salary
        HRA = float(input('\nPlease enter rent paid (In ₹)\n--> ')) - (0.1*basic_Salary)
        other_Allowances = float(input('\nPlease enter Other Allowances (In ₹)\n--> '))

        gross_Salary = basic_Salary+HRA+other_Allowances

        # Determine the professional tax rate based on the gross salary
        professional_tax_rate = 0  # No professional tax for gross salary up to ₹ 7,500
        if gross_Salary > 7500 and gross_Salary <= 10000:
            professional_tax_rate = 17.5
        elif gross_Salary > 10000:
            professional_tax_rate = 20.0

        # Provdidunt Fund rate is 12% in India
        pf_rate = 12

        # Determine the income tax rate based on the gross salary
        income_tax_rate = 0  # No income tax for gross salary below ₹ 2,50,000
        if gross_Salary > 1000000:
            income_tax_rate = 30
        elif gross_Salary > 500000:
            income_tax_rate = 20
        elif gross_Salary > 250000:
            income_tax_rate = 5

        # Calculate the tax amounts based on the gross salary
        professional_tax = (professional_tax_rate/100) * gross_Salary
        pf_deduction = (pf_rate / 100) * gross_Salary
        income_tax = (income_tax_rate / 100) * gross_Salary

        net_Salary = gross_Salary - professional_tax - pf_deduction - income_tax

        print(f'\nNet Salary :- ₹ {net_Salary} ')
        connector.close()
        exit()
    if option == '3':
        # HRA

        # HRA = Rent - 10% of basic salary
        HRA = float(input('\nPlease enter rent paid (In ₹)\n--> ')) - (0.1*basic_Salary)
        print(f'\nHRA :- ₹ {HRA} ')
    if option == '4':
        # DA

        # DA = daily allowance × number of days
        daily_Allowance = float(input('\nPlease enter the Daily Allowance (In ₹)\n--> '))
        number_Of_Days = int(input('\nPlease enter the number of days\n--> '))

        # Calculate DA by multiplying the daily allowance rate by the number of days
        DA = daily_Allowance * number_Of_Days

        print(f'Daily Allowance :- ₹ {DA}')

if option == '2':
    admin_Username = input('\nEnter Admin Username\n--> ')
    admin_Pwd = input('\nEnter Admin Password\n--> ')

    if admin_Username != 'Admin123':
        print(f"\n[ERROR] Wrong Username Entered. Please try again.")
        connector.close()
        exit()
    if admin_Pwd != 'Pwd1212':
        print(f"\n[ERROR] Wrong Password. Please try again.")
        connector.close()
        exit()

    option = input(
"""
Please Choose your option :
    1. Upload data of a new employee
    2. Check data of an employee
    3. Remove data of an employee
    4. Update employee details

--> """ )
    # If option is 1, then the program will ask to enter employee data
    if option == '1':
        # Getting data for database insertion
        while True: # A loop is added in case a user mistypes details
            name = input("\nPlease enter Employee Name\n--> ")
            phone = int(input("Please enter Employee's Phone number\n--> "))
            age = int(input("Please enter Employee's age\n--> "))
            dept = input("Please enter Employee's new department\n--> ")
            salary = float(input("Please enter Employee's salary\n--> "))
            pwd = input("Please enter Employee's Password\n--> ")
            option = input('\nAre you okay with the above details ? (Yes/No)\n--> ')

            if option in ('Yes','yes','Y','y'):
                break # Exits loop
            if option not in ('No','no','N','n'):
                print('\n[ERROR] Invalid response recevied please try again')
                connector.close()
                exit()
            # Program will bydefault restart loop if 'Yes' is not entered.
            # So a separate 'else' statement is not needed.

        print('\n[INFO] Writing to database')

        # Generating a new ID for the new employee
        query = connector.execute('SELECT Emp_ID from Empl;')
        data = query.fetchall()
        if data == []:
            emp_ID = 'EMP01'
        else:
            ID_List = []
            for i in data:
                ID_List.append(int(i[0][3:]))
            emp_No = max(ID_List)
            if emp_No < 10:
                emp_ID = f'EMP0{emp_No+1}'
            else:
                emp_ID = f'EMP{emp_No+1}'

        # Database insertion
        try:
            connector.execute(f"INSERT INTO Empl VALUES('{emp_ID}','{pwd}','{name}',{phone},{age},'{dept}',{salary})")
            connector.commit()
            print('\n[INFO] Employee details saved succesfully.')
        except:
            print('\n[ERROR] Write to database failed. Please try again.')

        connector.close()
        exit()

    # If option is 2, then the program will ask for the employee's ID
    if option == '2':
        # Retrieve ID of the employee from the user
        ID = input('\nPlease enter employee ID\n--> ')
        query = connector.execute(f"SELECT * FROM Empl WHERE Emp_ID = '{ID}';")
        empl_Data = query.fetchall()

        if empl_Data == []:
            print(f"\n[ERROR] No employee with ID '{ID}' found. Please try again.")
            connector.close()
            exit()
        # Prints out details of the employee
        print(f"""
        Employee Details :-
        Name        - {empl_Data[0][2]}
        Phone No.   - {empl_Data[0][3]}
        Age         - {empl_Data[0][4]}
        Department  - {empl_Data[0][5]}
        Salary      - {empl_Data[0][6]}
        """)
        connector.close()
        exit()

    # If option is 3, then the program will ask for employee's ID, for deletion
    if option == '3':
        # Retrieve ID of the employee from the user
        ID = input('\nPlease enter employee ID\n--> ')
        query = connector.execute(f"SELECT * FROM Empl WHERE Emp_ID = '{ID}';")
        empl_Data = query.fetchall()
        print(empl_Data)
        if empl_Data == []:
            print(f"\n[ERROR] No employee with ID '{ID}' found. Please try again.")
            connector.close()
            exit()

        # Confirmation for data deletion
        warn = input(f"[WARNING] Do you really want to delete the data of employee '{emp_Data[0][2]}' ?")
        if warn in ('No','no','N','n'):
            connector.close()
            exit()
        # Delete the data
        connector.execute(f"DELETE FROM Empl WHERE Emp_ID = '{ID}';")
        connector.commit()
        print('\n[INFO] Employee data was deleted successfully.')

        connector.close()
        exit()

    # If option is 4, then the program will ask for employee's ID, for data updation
    if option == '4':
        ID = input('\nPlease enter the employee ID whose details you want to update\n--> ')

        # Fetching the data of the employee
        query = connector.execute(f"SELECT * FROM Empl WHERE Emp_ID = '{ID}';")
        empl_Data = query.fetchall()
        if not empl_Data:
            print(f"\n[ERROR] No employee with ID '{ID}' found. Please try again.")
            connector.close()
            exit()

        print(f"""
        Employee Details:
        Name        - {empl_Data[0][2]}
        Phone No.   - {empl_Data[0][3]}
        Age         - {empl_Data[0][4]}
        Department  - {empl_Data[0][5]}
        Salary      - {empl_Data[0][6]}
        """)

        field_to_update = input('\nPlease enter the field you want to update (Name/Phone/Age/Department/Salary/Password):\n--> ')
        new_value = input(f'\nEnter the new value for {field_to_update}:\n--> ')

        update_query = f"UPDATE Empl SET {field_to_update} = '{new_value}' WHERE Emp_ID = '{ID}';"

        if field_to_update in ('Name', 'Phone', 'Age', 'Department', 'Salary', 'Password'):
            Dict = {'Name':'Emp_Name',
                    'Phone':'Emp_Phone',
                    'Age':'Emp_Age',
                    'Department':'Emp_Dept',
                    'Salary':'Emp_Salary',
                    'Password':'Emp_Pwd'}
            update_Query = f"UPDATE Empl SET {Dict[field_to_update]} = ? WHERE Emp_ID = ?;"
            try:
                connector.execute(update_Query, (new_value, ID))
                connector.commit()
                print(f'\n[INFO] Employee details updated successfully.')
            except:
                print(f'\n[ERROR] Update to the database failed. Please try again.')
        else:
            print(f"\n[ERROR] Invalid field name. Please use 'Name', 'Phone', 'Age', 'Department', 'Salary', or 'Password'.")

        connector.close()
        exit()
    # If the option entered is not 1,2 or 3, the program will exit
    else:
        print('\n[ERROR] Invalid response recevied please try again')
        connector.close()
        exit()


# If the option entered is not 1,2 or 3, the program will exit
else:
    print('\n[ERROR] Invalid response recevied please try again')
    connector.close()
    exit()