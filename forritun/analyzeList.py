def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True
        
# The main program starts here

def remove_duplicates_from_list(a_list):
    for i in range(len(a_list)-1, 0, -1):
        value = a_list[i]
        if a_list.index(value) != i:
            a_list.pop(i)

def main():
    csv_string = input("Enter integers separated with commas: ")
    try:
        input_list = [int(x) for x in csv_string.split(",")]
    except ValueError:
        print("Incorrect input!")
        return
    
    sorted_list = sorted(input_list)
    prime_list = [number for number in sorted_list if is_prime(number)]
    
    remove_duplicates_from_list(prime_list)
    
    average = sum(input_list) / len(input_list)
    
    print("Input list:", input_list)
    print("Sorted list: ", sorted(input_list))
    print("Prime list: ", prime_list)
    print("Min: {}, Max: {}, Average: {:.2f}".format(min(input_list), max(input_list), average))

main()