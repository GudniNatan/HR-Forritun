def make_new_row(old_row):
    new_row = [1]
    if len(old_row) == 0:
        return new_row
    for i in range(1, len(old_row)):
        value = old_row[i-1] + old_row[i]
        new_row.append(value)
    new_row.append(1)
    return new_row




# Main program starts here - DO NOT CHANGE
height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
    print(new_row)
