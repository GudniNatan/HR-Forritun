try:
    a =int(input())
except ValueError:
    print("cool")

try:
    print(5 / a)
except ZeroDivisionError:
    print("nope")
except NameError:
    print("very cool")