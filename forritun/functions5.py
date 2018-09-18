# palindrome function definition goes here
def palindrome(s):
    newString = ""
    for c in s:
        if c.isalpha():
            newString += c
    newString = newString.lower()
    return newString == newString[::-1]

in_str = input("Enter a string: ")

# call the function and print out the appropriate message
if palindrome(in_str):
    print('"' + in_str + '" is a palindrome.')
else:
    print('"' + in_str + '" is not a palindrome.')