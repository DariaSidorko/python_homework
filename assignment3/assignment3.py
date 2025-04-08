

import pandas as pd 

import json

# **************************************

#  Task 1: Introduction to Pandas - Creating and Manipulating DataFrames

# **************************************


# 1. Create a DataFrame from a dictionary:
data = {
    'Name': ['Alice', 'Bob', 'charlie'], 
    'Age': [25, 30, 35], 
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Convert to DataFrame
task1_data_frame = pd.DataFrame(data)


print(task1_data_frame)



# 2. Add a new column:

task1_with_salary = task1_data_frame.copy()

# Add Salary column
task1_with_salary['Salary'] = [70000, 80000, 90000]


print(task1_with_salary)



# 3. Modify an existing column:

task1_older = task1_with_salary.copy()

task1_older['Age'] += 1

print(task1_older)


# 4. Save the DataFrame as a CSV file:

task1_older.to_csv('employees.csv', index=False)

print(pd.read_csv('employees.csv'))



# **************************************

# Task 2: Loading Data from CSV and JSON

# **************************************


# 1. Read data from a CSV file:

task2_employees = pd.read_csv('employees.csv')

print(task2_employees)


# 2. Read data from a JSON file:

additional_employees = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]

# with open('additional_employees.json', 'w') as json_file:
#     json.dump(additional_employees, json_file)

json_employees = pd.read_json('additional_employees.json')

print(json_employees)


# 3. Combine DataFrames:

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)

print(more_employees)



# **************************************

# Task 3: Data Inspection - Using Head, Tail, and Info Methods

# **************************************


# 1. Use the head() method:

first_three = more_employees.head(3)

print(first_three)


# 2. Use the tail() method:

last_two = more_employees.tail(2)

print(last_two)


# 3. Get the shape of a DataFrame

employee_shape = more_employees.shape

print(employee_shape)


# 4. Use the info() method:

more_employees.info()



# **************************************

# Task 4: Data Cleaning

# **************************************


# 1. Load dirty data

dirty_data = pd.read_csv('dirty_data.csv')

print(dirty_data)

# 2.  Create a copy

clean_data = dirty_data.copy()

# 3. Remove duplicates

clean_data.drop_duplicates(inplace=True)

print(clean_data)

# 4. Convert Age to numeric and handle missing values

clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')

print(clean_data)

# 5. Convert Salary to numeric and replace placeholders

clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA, inplace=True)

clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')

print(clean_data)

# 6. Fill missing numeric values (Age with mean, Salary with median)

clean_data['Age'].fillna(clean_data['Age'].mean(), inplace=True)

clean_data['Salary'].fillna(clean_data['Salary'].median(), inplace=True)

print(clean_data)

# 7. Convert Hire Date to datetime

clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')

print(clean_data)

# 8. Standardize Name and Department

clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()

print(clean_data)


