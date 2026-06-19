contact = {}
for i in range(3):
    name = input("Enter the name: ")
    number = int(input("Enter the number: "))
    contact[name] = number
print("------------Contact Book-------------")
for name, number in contact.items():
    print(f"{name}: {number}")