hole = 1
while hole <= 18:
    par = int(input("Par of hole " + str(hole) + ": "))
    score = int(input("Score on hole " + str(hole) + ": "))
    
    total = score - par

    if total < -3:
        print("invalid score")
    elif total == -3:
        print("albatross")
    elif total == -2:
        print("eagle")
    elif total == -1:
        print("birdie")
    elif total == 0:
        print("par")
    elif total == 1:
        print("bogey")
    elif total == 2:
        print("double bogey")
    elif total == 3:
        print("triple bogey")
    else:
        print("bad hole")

    hole += 1