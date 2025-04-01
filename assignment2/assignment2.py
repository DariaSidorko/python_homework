import csv
import traceback

# Task 2: Read a CSV File
def read_employees():
    employees = {"fields": [], "rows": []}
    try:
        with open("../csv/employees.csv", "r", newline="") as file:
            reader = csv.reader(file)
            employees["fields"] = next(reader)
            employees["rows"] = [row for row in reader]
        return employees
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = [f'File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}' for trace in trace_back]
        print(f"Exception type: {type(e).__name__}")
        if str(e):
            print(f"Exception message: {str(e)}")
        print(f"Stack trace: {stack_trace}")
        return None

employees = read_employees()
print(employees)

# Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

# Task 4: Find the Employee First Name
def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    return list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]

#Task 8: Create a dict for an Employee
def employee_dict(row):
    return {key: value for key, value in zip(employees["fields"][1:], row[1:])}

# print("Result:")
# print(employees["row"][3])
#print(employee_dict())


#Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    return {row[employee_id_column]: employee_dict(row) for row in employees["rows"]}

print(all_employees_dict())

# Task 10: Use the os Module
import os

def get_this_value():
    return os.getenv("THISVALUE")

# Task 11: Creating custom_module.py
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

# set_that_secret("abracadabra")
# print(custom_module.secret) 
    
# Task 12: Read minutes1.csv and minutes2.csv
    
def read_minutes():
    def read_file(file_name):
        minutes = {"fields": [], "rows": []}
        try:
            with open(file_name, "r", newline="") as file:
                reader = csv.reader(file)
                minutes["fields"] = next(reader)
                minutes["rows"] = [tuple(row) for row in reader]  # Convert rows to tuples
            return minutes
        except Exception as e:
            print(f"Error reading {file_name}: {e}")
            return None

    minutes1 = read_file("../csv/minutes1.csv")
    minutes2 = read_file("../csv/minutes2.csv")
    return minutes1, minutes2

# Store globally
minutes1, minutes2 = read_minutes()
print(minutes1, minutes2)


# Task 13: Create minutes_set

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1 | set2  # Union of both sets

# Store globally
minutes_set = create_minutes_set()
print(minutes_set)


# Task 14: Convert to datetime

from datetime import datetime

def create_minutes_list():
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))

# Store globally
minutes_list = create_minutes_list()
print(minutes_list)

# Task 15: Write Out Sorted List

def write_sorted_list():
    # Sort by datetime
    minutes_list.sort(key=lambda x: x[1])

    # Convert datetime back to string
    formatted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))

    # Write to file
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])  # Write headers
        writer.writerows(formatted_list)  # Write sorted data

    return formatted_list

# Call the function and verify the file
sorted_minutes = write_sorted_list()
print(sorted_minutes)
