while True:
    print ("1.Add student")
    print ("2.View tudent")
    print ("3.Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter a student name: ")
        marks = input("Enter marks :")
    
        file = open("student.txt","a")
        file.write(name + ","+ marks +"\n")
        file.close()
        print(" Student  added successfully ")
    
    elif choice == 2:
        file = open("student.txt","r")
        content = file.read()
        print(content)
        file.close()
        
    elif choice == 3:
        print("Exit")    
        break
        
    else:
        print("invalid choice")
        
        