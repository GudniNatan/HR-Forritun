# Gudni Natan Gunnarsson 
# 26.9.2018
# Skilaverkefni 5

import random
import string

def scramble_word(word):
    if len(word) < 4:
        return word
    end = -1
    if word[end] in string.punctuation: # The word is ended with punctuation
        end = -2
    char_list = list(word[1:end])
    random.shuffle(char_list)
    scrambled = word[0] + "".join(char_list) + word[end:]
    return scrambled

def get_word_string(filename):
    try:
        file = open(filename)
        word_string = ""
        for line in file:
            word_string += line.strip() + " "
        return word_string
    except FileNotFoundError:
        print("File", filename, "not found")
        return ""

def scramble_string(word_string):
    word_list = word_string.split()
    for i, word in enumerate(word_list):
        word_list[i] = scramble_word(word)
    scrmbl_str = str()
    for word in word_list:
        scrmbl_str += word + " "
    return scrmbl_str

# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)
