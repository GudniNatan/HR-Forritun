longestword = ""
lengthOfLongest = 0
try:
    with open("words.txt") as file:
        for line in file:
            line = line.strip()
            if len(line) > lengthOfLongest:
                longestword = line
                lengthOfLongest = len(line)
except:
    print("error")

print("Longest word is '" + longestword  + "' of length " + str(lengthOfLongest))