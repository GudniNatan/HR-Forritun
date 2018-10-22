def menu_selection():
    print("Menu: ")
    choice = input("add(a), remove(r), find(f): ").lower()
    return choice


def dict_to_tuples(a_dict):
    return [(key, value) for key, value in a_dict.items()]


def add_to_dict(a_dict):
    key = input("Key: ")
    value = input("Value: ")
    if key in a_dict:
        print("Error. Key already exists.")
    else:
        a_dict[key] = value


def remove_from_dict(a_dict):
    key = input("key to remove: ")
    try:
        a_dict.pop(key)
    except KeyError:
        print("No such key exists in the dictionary.")


def find_key(a_dict):
    key = input("Key to locate: ")
    try:
        print("Value: ", a_dict[key])
    except KeyError:
        print("Key not found.")


def execute_selection(choice, a_dict):
    functions = {"a": add_to_dict, "r": remove_from_dict, "f": find_key}
    try:
        functions[choice](a_dict)
    except KeyError:
        print("Invalid choice.")


# Do not change this main function
def main():
    more = True
    a_dict = {}
    
    while more:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more = again.lower() == 'y'
    
    dictlist = dict_to_tuples(a_dict)
    print(sorted(dictlist))

main()