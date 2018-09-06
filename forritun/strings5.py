s = input("Input a string: ")
output = ""
for c in s:
    if c.isdigit():
        output += c
print(output)