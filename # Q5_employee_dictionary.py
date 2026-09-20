# Q5_employee_dictionary.py

employees = {
    "E1": {
        "Employee Name": "Rahul",
        "Designation": "Manager",
        "Department": "HR",
        "Salary": 50000
    },

    "E2": {
        "Employee Name": "Amit",
        "Designation": "Developer",
        "Department": "IT",
        "Salary": 65000
    },

    "E3": {
        "Employee Name": "Riya",
        "Designation": "Designer",
        "Department": "Design",
        "Salary": 55000
    },

    "E4": {
        "Employee Name": "Sayan",
        "Designation": "Developer",
        "Department": "IT",
        "Salary": 70000
    },

    "E5": {
        "Employee Name": "Priya",
        "Designation": "Tester",
        "Department": "QA",
        "Salary": 48000
    }
}

# 1. Print record of E1
print("Record of Employee E1:")
print(employees["E1"])

# 2. Department of E4
print("\nDepartment of E4:")
print(employees["E4"]["Department"])

# 3. Employee with maximum salary
max_employee = max(
    employees,
    key=lambda employee: employees[employee]["Salary"]
)

print("\nEmployee with maximum salary:")
print(max_employee)
print(employees[max_employee])

# 4. Insert new employee
employees["E6"] = {
    "Employee Name": "Karan",
    "Designation": "Developer",
    "Department": "IT",
    "Salary": 60000
}

print("\nUpdated Employee Dictionary:")
print(employees)
