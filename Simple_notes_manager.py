file = open("note.txt","w")
file.write( "sorry")
file.close()

file = open("note.txt","r")
content = file.read()
print(content)
file.close()
