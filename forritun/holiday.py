month = input("Month: ")
day = input("Day: ")

date = month.capitalize() + " " + day

if date == "January 1":
    print("New year's day")
elif date == "June 17":
    print("National holiday")
elif date == "December 25":
    print("Christmas day")
else:
    print("Not a holiday")