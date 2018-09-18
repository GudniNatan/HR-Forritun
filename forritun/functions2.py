# Your function definition goes here
def count_case(s):
    upper = 0
    lower = 0
    for c in s:
        if c.islower():
            lower += 1
        elif c.isupper():
            upper += 1
    return upper, lower


user_input = input("Enter a string: ")

# Call the function here
upper, lower = count_case(user_input)
print("Upper case count: ", upper)
print("Lower case count: ", lower)