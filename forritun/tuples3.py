def even_sum(str_list):
    int_list = [int(x) for x in str_list if int(x) % 2 == 0]
    return sum(int_list)


def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))
