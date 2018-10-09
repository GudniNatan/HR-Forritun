import string
#build_wordlist() function goes here
def build_wordlist(io_stream):
    word_list = list()
    for line in io_stream:
        for punct in string.punctuation:
            line = line.replace(punct, "")
        words = line.split()
        word_list.extend(words)
    return word_list

#find_unique() function goes here
def find_unique(word_list):
    new_list = list()
    for word in word_list:
        if word not in new_list:
            new_list.append(word)
    return new_list

def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)  
    infile.close()  
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()