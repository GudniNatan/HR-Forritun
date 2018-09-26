inputFile = open("words.txt", "r")
outputFile = open("sentences.txt", "w")

for line in inputFile:
    if line.strip() == "":
        outputFile.write("\n")
        print()
    else:
        word = line.replace("\n", "") + " "
        outputFile.write(word)
        print(word, end="")
print()

inputFile.close()
outputFile.close()