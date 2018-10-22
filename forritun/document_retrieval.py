import string

# Gudni Natan Gunnarsson
# 22.10.2018
# Skilaverkefni 8


def bookmarkWords(bookmark_dict, document, document_id):
    for word in document.split():
        word = word.lower().strip(string.punctuation)
        try:
            bookmark_dict[word].append(document_id)
        except KeyError:
            bookmark_dict[word] = [document_id]


def openFile(filename):
    file = list()
    try:
        with open(filename) as file_pointer:
            file.extend(file_pointer)  # Load entire file into a list.
    except FileNotFoundError:
        print("Documents not found.")
    return file


def processDocument(single_document, document_list, word_reference_dict):
    single_document = single_document.strip()
    document_number = len(document_list)
    document_list.append(single_document)
    bookmarkWords(word_reference_dict, single_document, document_number)


def readFileDocuments(file_list):
    document_list = list()
    word_reference_dict = dict()
    single_document = ""
    file_list.pop(0)  # Ignore the first line, as it just declares the first doc.
    for line in file_list:
        if line == "<NEW DOCUMENT>\n":
            processDocument(single_document, document_list, word_reference_dict)
            single_document = ""
        else:
            single_document += line
    processDocument(single_document, document_list, word_reference_dict)
    return document_list, word_reference_dict


def printWordSearchResult(matching_documents):
    print("Documents that fit search:", end=" ")
    for result in matching_documents:
        print(result, end=" ")
    print()


def wordSearch(bookmark_dict):
    search_words = input("Enter search words: ").split()
    try:
        first_results = bookmark_dict[search_words[0]]
        matching_documents = set(first_results)
        for term in search_words:
            ith_word_documents = set(bookmark_dict[term])
            matching_documents &= ith_word_documents  # narrow down search
    except KeyError:
        print("No match.")
        return
    printWordSearchResult(matching_documents)


def printDocument(documents):
    doc_num_str = input("Enter document number: ")
    try:
        doc_num = int(doc_num_str)
    except ValueError:
        print("Not a number!")
        return
    print("Document #{}".format(doc_num))
    try:
        print(documents[doc_num])
    except IndexError:
        print("Document", doc_num, "does not exist!")


def getUserMenuResponse():
    print("\nWhat would you like to do?")
    print("1. Search Documents")
    print("2. Print Document")
    print("3. Quit Program")
    response = input("> ")
    return response


def menu(document_list, bookmark_dict):
    response = "1"
    while response == "1" or response == "2":
        response = getUserMenuResponse()
        if response == "1":
            wordSearch(bookmark_dict)
        elif response == "2":
            printDocument(document_list)
    print("Exiting program.")


def main():
    filename = input("Document collection: ")
    file = openFile(filename)
    if file:
        document_list, bookmark_dict = readFileDocuments(file)
        menu(document_list, bookmark_dict)


main()
