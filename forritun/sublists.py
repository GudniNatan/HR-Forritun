def make_sublists(a_list):
    sub_lists = list()
    sub_lists.append([])
    for i in range(len(a_list)+1):
        for j in range(i + 1, len(a_list)+1):
            sub_lists.append(a_list[i:j])
    return sub_lists
# Main program starts here
def main():
    input_list = input("Enter a list separated with commas: ").split(",")
    sub_lists = make_sublists(input_list)
    # This should be the last statement in your main program/function 
    print(sorted(sub_lists))

main()