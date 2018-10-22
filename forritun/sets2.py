def make_set_of_ints(csv_string):
    str_list = csv_string.split(",")
    int_set = set()
    for num_str in str_list:
        num_int = int(num_str)
        int_set.add(num_int)
    return int_set


def print_set_intersection(set_a, set_b):
    intersection = set_a.intersection(set_b)
    print(intersection)


def print_set_union(set_a, set_b):
    union = set_a.union(set_b)
    print(union)


def print_set_difference(set_a, set_b):
    difference = set_a.difference(set_b)
    print(difference)


def main():
    a_string = input("Input a list of integers separated with a comma: ")
    b_string = input("Input a list of integers separated with a comma: ")
    set_a = make_set_of_ints(a_string)
    set_b = make_set_of_ints(b_string)

    print(set_a)
    print(set_b)

    selection = ""
    while selection != "4":
        print("1. Intersection\n2. Union\n3. Difference\n4. Quit")
        selection = input("Set operation: ")
        if selection == "1":
            print_set_intersection(set_a, set_b)
        elif selection == "2":
            print_set_union(set_a, set_b)
        elif selection == "3":
            print_set_difference(set_a, set_b)


main()
