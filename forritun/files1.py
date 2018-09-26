file = open("test.txt")

for line in file:
    print(line.strip().replace(" ", ""), end="")

file.close()