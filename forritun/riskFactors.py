# Gudni Natan Gunnarsson
# Skilaverkefni 6
# 2.10.2018

"""
Columns of interest:
Heart Disease Death Rate =  1
Motor Vehicle Death Rate = 5
Teen Birth Rate = 7
Adult Smoking = 11
Adult Obesity = 13
"""
COLS_OF_INTEREST = (1, 5, 7, 11, 13)


def numerify_CSV_row(row):
    '''Read row of CSV file, remove % signs and convert to float if possible. Returns the updated row as a list.'''
    value_list = row.split(",")
    for i, value in enumerate(value_list):
        value = value.replace("%", "")
        try:
            value_list[i] = float(value)
        except ValueError:
            if value == "N/A":
                value_list[i] = None
    return value_list


def read_CSV_file(filename):
    '''Read the CSV file located at 'filename'. Returns the head, the table. Prints error and returns none if FileNotFound.'''
    try:
        csv_file = open(filename)
    except FileNotFoundError:
        print("Cannot find file", filename)
        return None, None
    table = [numerify_CSV_row(line) for line in csv_file]
    csv_file.close()
    head = table.pop(0)
    return head, table


def getCandidates(table, colNum):
    '''Returns the values from the colNum along with the accompanying state. Ignores N/A values.'''
    candidates = [(row[colNum], row[0]) for row in table if row[colNum] is not None] # col 0 is the state name
    return candidates


def output_column_info(table, head, colNum):
    '''Output the min/max info of the specified colNum'''
    candidates = getCandidates(table, colNum)
    minNumber, minState  = min(candidates)
    maxNumber, maxState = max(candidates)

    title = head[colNum] + ":"
    print("{:<33}{:<21}{:>6.1f}{:<6}{:<15}{:>6.1f}".format(title, minState, minNumber, "", maxState, maxNumber))

def main():
    filename = input("Enter filename containing csv data: ")
    head, table = read_CSV_file(filename)
    print("{:<33}{:<21}{:12}{:<21}".format("Indicator", "Min", "", "Max"))
    print("-" * 87)
    if head and table:
        for index in COLS_OF_INTEREST:
            output_column_info(table, head, index)

main()
