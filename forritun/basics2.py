import math

x1_str = input("Input x1: ")  # do not change this line
y1_str = input("Input y1: ")  # do not change this line
x2_str = input("Input x2: ")  # do not change this line
y2_str = input("Input y2: ")  # do not change this line

# convert strings to ints
(x1, x2, y1, y2) = (int(x1_str), int(x2_str), int(y1_str), int(y2_str))
d = ((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2)) ** 0.5
print("d =",d)  # do not change this line