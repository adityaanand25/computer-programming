#You have a dictionary containing employee IDs as keys and their names as values. Write a program to find the name of the employee with a specific ID.
python

employees = {101: 'Alice', 102: 'Bob', 103: 'Charlie'}
employee_id = 102
employee_name = employees.get(employee_id, 'Not Found')
print(employee_name)
