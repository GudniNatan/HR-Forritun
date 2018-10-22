import string
def cleanWord(word):
    word = word.strip().lower()
    for punct in string.punctuation:
        if word[-1] == punct:
            word = word[:-1]
    return word

def get_word_list(file_object):
    words = list()
    for line in file_object:
        for word in line.split():
            clean = cleanWord(word)
            words.append(clean)
    return words

def word_list_to_counts(word_list):
    word_count_dict = dict()
    for word in word_list:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    return word_count_dict

def dict_to_tuple(a_dict):
    return [(key, value) for key, value in a_dict.items()]

def main():
    filename = input("Name of file: ")
    # Get a file pointer
    fpointer = open(filename)
    # Get a list of words from the file
    word_list = get_word_list(fpointer) 
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuple(word_count_dict)
    print(sorted(word_count_tuples))
    
main()