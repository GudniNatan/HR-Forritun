# Function definitions start here
def open_file(filename):
    try:
        file = open(filename)
        return file
    except FileNotFoundError:
        return None

def get_longest_word(file_stream):
    words = [word.strip() for word in file_stream]
    return max(words, key=len)

# The main program starts here
filename = input("Enter name of file: ")
file_stream = open_file(filename)
if file_stream:
	longest_word = get_longest_word(file_stream)
	print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
	file_stream.close()
else:
	print('File',filename,'not found!')