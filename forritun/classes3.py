class Sentence():

    def __init__(self, sentance):
        self.sentance = sentance
        self.words = sentance.split()

    def get_first_word(self):
        return self.words[0]

    def get_all_words(self):
        return self.words

    def replace(self, index, new_word):
        try:
            self.words[index] = new_word
        except IndexError:
            pass
