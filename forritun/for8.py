stars = int(input("Max number of stars: ")) # Do not change this line

for i in range(1, stars):
    print(i * "*")

for i in range(stars, 0, -1):
    print(i * "*")
