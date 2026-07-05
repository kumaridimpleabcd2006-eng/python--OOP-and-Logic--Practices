record = input("Enter the student name and Marks : ")

file = open("note.txt","w")
content = file.write(record)
file.close()

file = open("note.txt","r")
content = file.read()
print("student record")
print(content)
file.close()
