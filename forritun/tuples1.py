def mutate_list(a_list, index_num, v):
    ''' Inserts v at index index_num in a_list'''
    a_list.insert(index_num, v)
    
def remove_ch(a_list, index_num):
    ''' Removes character at index_num from a_list'''
    a_list.pop(index_num)
    
def get_list():
    ''' Reads in values for a list and returns the list '''
    user_list = input("Enter values in list separated by commas: ")
    user_list = user_list.split(",")
    user_list = [int(i) for i in user_list]
    return user_list

# Main program starts here
values = get_list()
print(values)

choice = input("Enter choice (m,r): ")
if choice == "m":
    index, v = [int(x) for x in input().split(",")]
    mutate_list(values, index, v)
elif choice == "r":
    index = int(input())
    remove_ch(values, index)

print(values)