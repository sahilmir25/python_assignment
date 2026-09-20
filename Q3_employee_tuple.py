# Q3_employee_tuple.py

employees = (
    "Rahul", "Amit", "Sayan", "Riya", "Priya",
    "Rahul", "Ankit", "Neha", "Riya", "Rohit",
    "Sneha", "Amit", "Karan", "Priya", "Rahul",
    "Neha", "Sayan", "Rohit", "Rahul", "Karan"
)

# 1. Print each name and frequency
print("Employee Name and Frequency:")

for name in set(employees):
    print(name, ":", employees.count(name))

# 2. Remove duplicate items
distinct_names = tuple(set(employees))

print("\nDistinct employee names:")
print(distinct_names)

# 3. Employee having maximum frequency
max_frequency = max(employees.count(name) for name in set(employees))

for name in set(employees):
    if employees.count(name) == max_frequency:
        print("\nEmployee with maximum frequency:", name)
        print("Frequency:", max_frequency)

# 4. Sort alphabetically
sorted_employees = tuple(sorted(employees))

print("\nEmployees in alphabetical order:")
print(sorted_employees)

# 5. Search employee
search_name = input("\nEnter employee name to search: ")

if search_name in employees:
    print(search_name, "exists in the tuple.")
else:
    print(search_name, "does not exist in the tuple.")
