class MyString:
    def __init__(self, string):
        self.string = string

    def __sub__(self, other):
        return len(self.string) - len(other.string)

    def __gt__(self, other):
        return len(self.string) > len(other.string)
