import curses.ascii as ascii
string = input()

for c in string:
    if ascii.isLower(c):
        print(c)