library = {}
while True:
    print("1. Add Book ")
    print("2. View Books ")
    print("3. Search Book ")
    print("4. Update Author ")
    print("5. Delete Book ")
    print("6. Total Books ")
    print("Exit")
    
    choice = int(input("Enter your choice : "))
    if choice == 1:
        book = input("Enter your book name : ")
        author = input("Enter your author name : ")
        library[book] = author
        
    elif choice == 2:
        for books,author in library.items():
            print(f"Book:{book},Author:{author}")
            
    elif choice == 3:
        book = input("Enter book name ")
        if  book in library:
            print("library[book]")
        else:
            print("books are not found ")
        
    elif choice == 4:
        book = input("Enter book name") 
        if book in library:
            author = input("Enter new author ")
            library[book] = author
     
    elif choice == 5:
        book = input("Enter book name ")  
        if book in library:    
           del library[book]  
        else:
            print("Book not found") 
        
    elif choice == 6:  
        print("Total Book",len(library))  
    elif choice == 7:     
        break  
    else:
        print("invalid")
                       
          
        
                    


