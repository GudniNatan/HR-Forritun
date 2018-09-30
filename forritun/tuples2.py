#list_to_tuple function goes here
def list_to_tuple(a_list):
    try:
        return tuple(int(x) for x in a_list)
    except ValueError:
        print("Error. Please enter only integers.")
        return tuple()

# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)
