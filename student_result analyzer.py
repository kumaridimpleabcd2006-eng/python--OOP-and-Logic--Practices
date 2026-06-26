marks =[78,92,65,88,95]
total = sum(marks)
print(f"Total Marks: {total}")

average = total/len(marks)
print(f"Average Marks: {average}")

highest = max(marks)
print(f"Highest Marks: {highest}")

lowest = min(marks)
print(f"Lowest Marks: {lowest}")

student =len(marks)
print(f"No. of Student : {student}")

for i in marks:
    if i>=40:
        print(f"{i}pass")
    else:
        print(f"{i}Fail")    
