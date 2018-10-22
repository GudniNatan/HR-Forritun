import string


def read_file_to_list(file_pointer):
    file_list = list()
    for line in file_pointer:
        words = line.lower().split()
        for i in range(len(words)):
            for punct in string.punctuation:
                words[i] = words[i].replace(punct, "")
        file_list.extend(words)
    return file_list


def countBigrams(word_list):
    count_tracking_dict = dict()
    last_word = None
    for word in word_list:
        if last_word is None:
            last_word = word
            continue
        bigram = (last_word, word)
        try:
            count_tracking_dict[bigram] += 1
        except KeyError:
            count_tracking_dict[bigram] = 1
        last_word = word
    return [(x, y) for x, y in count_tracking_dict.items()]


def returnSecondValue(a_tuple):
    return -a_tuple[1]


def main():
    filename = input("Enter name of file: ")
    try:
        file_pointer = open(filename)  # could break
    except FileNotFoundError:
        print("File not found, exiting")
        return
    word_list = read_file_to_list(file_pointer)
    file_pointer.close()
    bigram_count = countBigrams(word_list)
    bigram_count.sort(key=returnSecondValue)
    print(bigram_count[:10])


main()
