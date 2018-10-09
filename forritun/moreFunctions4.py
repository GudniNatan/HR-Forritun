def merge_lists(list_a, list_b):
    concat = list_a + list_b
    new_list = list()
    for element in concat:
        if element not in new_list:
            new_list.append(element)
    new_list.sort()
    return new_list

# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
