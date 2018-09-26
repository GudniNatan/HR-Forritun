# Gudni Natan
# 18.9.2018
# Forritun

def getShares():
    while True:
        shares_str = input("Enter number of shares: ")
        try:
            shares_int = int(shares_str)
            return shares_int
        except ValueError: 
            print("Invalid number!")

def getPrice():
    while True:
        try:
            dollars_str, numerator_str, denominator_str = input("Enter price (dollars, numerator, denominator): ").split()
            dollars_int = int(dollars_str)
            numerator_int = int(numerator_str)
            denominator_int = int(denominator_str)
            return dollars_int, numerator_int, denominator_int
        except ValueError:
            print("Invalid price!")

def outputValue(shares, dollars, numerator, denominator):
    value = shares * (dollars + (numerator / denominator))
    print("{} shares with market price {} {}/{} have value ${:.2f}".format(shares, dollars, numerator, denominator, value))



cont = "y"

while cont.lower() == "y":
    shares = getShares()
    dollars, numerator, denominator = getPrice()
    outputValue(shares, dollars, numerator, denominator)
    cont = input("Continue: ")