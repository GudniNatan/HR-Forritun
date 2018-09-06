name = input("Input a name: ")
lastname, firstname = name.split(", ")
outName = firstname[0].upper() + ". " + lastname.title()
print(outName)