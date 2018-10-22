def main():
    my_dict = dict()
    more = "y"
    while more.lower() == "y":
        name = input("Name: ")
        number = input("Number: ")
        my_dict[name] = number
        more = input("More data (y/n)? ")
    tuples = [(key, value) for key, value in my_dict.items()]
    print(sorted(tuples))

main()