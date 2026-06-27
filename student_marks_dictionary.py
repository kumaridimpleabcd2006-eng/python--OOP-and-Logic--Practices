student = {
    "Rahul": 85,
    "Priya": 92,
    "Aman": 76,
    "Neha": 95
}

# Total Marks
total = sum(student.values())
print("Total Marks:", total)

# Average Marks
average = total / len(student)
print("Average Marks:", average)

# Highest Marks
highest = max(student, key=student.get)
print("Highest Marks:", highest, student[highest])

# Lowest Marks
lowest = min(student, key=student.get)
print("Lowest Marks:", lowest, student[lowest])

# Pass Students (Marks >= 40)
print("\nPass Students:")
for name, marks in student.items():
    if marks >= 40:
        print(name, marks)

# Total Students
print("\nTotal Students:", len(student))
    
