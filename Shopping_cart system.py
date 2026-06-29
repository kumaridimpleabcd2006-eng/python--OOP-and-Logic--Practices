cart = {}
while True:
    print("1. Add items")
    print("2.View Cart")
    print("3. Search I]items")
    print("4.Upgate quantity")
    print("5.Remove items")
    print("6.Caluate Total items")
    print("7.Exit")
    choice = int(input("Enter your Choices : "))
    
    if choice == 1: 
        items = input("Enter your name: ")
        quantity = int(input("Enter your quantity : "))
        cart[items]=quantity 
        print("items successfully add")
        
    elif choice == 2: 
        if cart:
             for items ,quantity in cart.items():
                print(f"items: {items}, quantity: {quantity}")
        else :
            print("cart is empty")
    elif choice == 3:
         items = input("Enter your name: ")
         if items in cart:
             print(f"items: {items}, quantity: {cart[items]}")
         else :
             print("items are not found")
    elif choice == 4:
        items = input("Enter your name: ")
        if items in cart:
            quantity = int(input("Enter new quantity: "))
            cart[items] = quantity
            print("items are successfully updated")
        else:
            print("items are not found")
    elif choice == 5:
         items = input("Enter your name: ")
         if items in cart:
            del cart[items]
            print("items successfully removed")
         else:
           print("items are not found") 
           
    elif choice == 6:  
        total = sum(cart.values())
        print(f"total items: {total}")
    elif choice == 7:       
        print("thankyou")
        break
    else:
       print("invalid choice")
         
                
                 
         
                
            
        
            
          
        
    
    
    
