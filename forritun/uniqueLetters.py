import string

sentence = input("Input a sentence: ")

# Here you should add the missing part
unique_letters = list()
for i, c in enumerate(sentence):
    if c.isalnum() and sentence.index(c) == i:
        unique_letters.append(c)

print("Unique letters:", unique_letters)
