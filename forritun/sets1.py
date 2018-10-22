def commonLettersList(firstName, lastName):
    common = list()
    for character in firstName:
        if character in lastName and character not in common:
            common.append(character)
    return common


def commonLettersSet(firstName, lastName):
    firstCharacters = set(firstName)
    lastCharacters = set(lastName)
    common = firstCharacters & lastCharacters
    return common


def main():
    firstName, lastName = input("Enter name: ").split()
    firstName = firstName.lower()
    lastName = lastName.lower()
    commonList = commonLettersList(firstName, lastName)
    commonSet = commonLettersSet(firstName, lastName)

    print(sorted(commonList))
    print(sorted(commonSet))

main()
