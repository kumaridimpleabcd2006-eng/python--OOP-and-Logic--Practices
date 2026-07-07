contact = {}
while True:
    print("1. Add contact")
    print("2. View conact")
    print("3. Delete conact")
    print("4. Exit")
    
    choice = int(input("Enter a choice: "))
    if choice == 1:
        name =input("Enter a name ")
        phone = int(input("Enter a Add contact "))
        
        contact[name] =  phone
        print("sucessfully add")
        
    elif choice == 2: 
        if len(contact) == 0:
          print("no contact found") 
        else:
          print("\n --- contact list ---")  
             
        for name in contact:
            print(f"{name},{phone}")
            print("View contact")
    elif choice == 3:
        name = input("Enter a delete name ")
        if name in contact:
          del contact[name]
          print("sucessfully delete")
        
        
    elif choice == 4:
         print("Exit")    
         break
    else:
        print("inva;id choice")
    
            
            
             
        