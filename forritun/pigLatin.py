# Gudni Natan Gunnarsson
# 6.9.2018
# Forritun
vowels = "aeiou"
while True:
    s = input("Enter a word: ")
    if s == ".":
        break
    for i in range(len(s)):
        if s[i] in vowels:
            if i == 0:
                print(s + "yay")
            else:
                print(s[i:] + s[:i] + "ay")
            break
    else:
        print(s)
