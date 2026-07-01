file = open("note.txt","w")
file.write("helllo kitty")
file.close()



file = open("note.txt","r")
content = file.read()
print(content)
file.close()