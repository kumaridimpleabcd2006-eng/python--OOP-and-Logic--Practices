
employee = {
    "Rahul": 25000,
    "Priya": 30000,
    "Aman": 28000
}

search_name = input("Enter employee name: ")

if search_name in employee:
    print(f"Salary of {search_name}: {employee[search_name]}")
else:
    print("Employee not found")
