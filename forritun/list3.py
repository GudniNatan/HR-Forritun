# Your functions should appear here
def populate_list(initalList):
    value = input("Enter value to be added to list: ")
    while value.lower() != "exit":
        initalList.append(value)
        value = input("Enter value to be added to list: ")

def triple_list(initalList):
    return initalList * 3

# Main program starts here - DO NOT change it.
initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)
