while True:
    print("A 100-85")
    print("B 85-75")
    print("C 75-65")
    print("D 65-55")
    print("E  below 55")
    print("Exit")
    choice = input("Enter your choice :")
    
    if choice == "A":
         print("GRADE A")
    elif choice == "B":
         print("GRADE B")
    elif choice == "C":
         print("GRADE C")
    elif choice == "D":
          print("GRADE D")
    elif choice == "E":
          print("your are failed")
    elif choice == "Exit":
          print("Good Bye")
          break
    else:
      print("invalid choice")
