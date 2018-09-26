import random
import string

def get_word_string(filename):
    try:
        file = open(filename)
        
    return ""

def scramble_string(word_string):
    random.shuffle(word_string)
    return word_string

# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)