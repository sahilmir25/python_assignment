# Q2_marks_analysis.py

marks = [
    65, 78, 85, 90, 72,
    85, 68, 90, 75, 85,
    92, 78, 85, 70, 90,
    85, 76, 88, 85, 80
]

# 1. Average marks
average = sum(marks) / len(marks)

print("Average marks:", average)

# 2. Students scoring more than average
count = 0

for mark in marks:
    if mark > average:
        count += 1

print("Students scoring more than average:", count)

# 3. Maximum frequency of marks
frequency = {}

for mark in marks:
    frequency[mark] = frequency.get(mark, 0) + 1

max_frequency = max(frequency.values())

print("Maximum frequency:", max_frequency)

print("Marks scored by maximum students:")

for mark, freq in frequency.items():
    if freq == max_frequency:
        print(mark)
