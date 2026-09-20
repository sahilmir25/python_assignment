# Q1_student_marks.py

students = [
    "Rahul", "Amit", "Sayan", "Riya", "Priya",
    "Ankit", "Neha", "Rohit", "Sneha", "Karan"
]

marks = [85, 72, 91, 68, 95, 78, 88, 74, 82, 90]

# Maximum and minimum marks
max_marks = max(marks)
min_marks = min(marks)

max_index = marks.index(max_marks)
min_index = marks.index(min_marks)

print("Student with maximum marks:", students[max_index])
print("Maximum marks:", max_marks)

print("Student with minimum marks:", students[min_index])
print("Minimum marks:", min_marks)
