
import pandas as pd

df = pd.read_csv('../csv/employees.csv')

employee_names = [f"{row['first_name']} {row['last_name']}" for _, row in df.iterrows()]
print("All employee names:")
print(employee_names)

names_with_e = [name for name in employee_names if 'e' in name.lower()]
print("\nEmployee names containing the letter 'e':")
print(names_with_e)
