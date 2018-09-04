# Skilaverkefni I
# Gudni Natan Gunnarsson
# 28.8.2018
debt = float(input("Input the cost of the item in $: "))

interestAmount = 0.015 
if debt > 1000:
    interestAmount = 0.02

month = 0
totalInterests = 0

while debt > 0:
    month += 1
    interest = debt * interestAmount
    
    totalInterests += interest

    debt += interest
    payment = debt
    if debt > 50.0:
        payment = 50.0
        debt -= payment
    else:
        debt = 0 

    print("Month: " + str(month) + 
        " Payment: " + str(round(payment, 2)) + 
        " Interest paid: " + str(round(interest, 2)) +
        " Remaining debt: " + str(round(debt, 2)))

print("\nNumber of months: " + str(month))
print("Total interest paid: " + str(round(totalInterests,2)))