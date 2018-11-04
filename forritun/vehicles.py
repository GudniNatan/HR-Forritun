class Vehicle(object):
    def __init__(self, the_license, the_year):
        try:
            self.year = int(the_year)
        except:
            self.year = 0
        self.license = str(the_license)
        self.weight = 0.0
        self.fee = 0.0

    def get_license(self):
        return self.license

    def get_year(self):
        return self.year

    def get_weight(self):
        return self.weight

    def get_fee(self):
        return self.fee

    def set_weight(self, the_weight):
        try:
            self.weight = float(the_weight)
        except ValueError:
            self.weight = 0.0

    def set_fee(self, the_fee):
        try:
            self.fee = float(the_fee)
        except ValueError:
            self.fee = 0.0

    def __str__(self):
        return "Vehicle: {} {} Weight={:.2f} Fee=${:.2f}".format(
            self.get_license(), self.get_year(), self.get_weight(),
            self.get_fee())


class Car(Vehicle):
    def __init__(self, the_license, the_year, the_style):
        super().__init__(the_license, the_year)
        try:
            self.style = str(the_style)
        except ValueError:
            self.style = ""

    def set_weight(self, the_weight):
        super().set_weight(the_weight)
        if self.get_weight() < 3000:
            self.set_fee(30)
        elif self.get_weight() < 5000:
            self.set_fee(40)
        else:
            self.set_fee(50)

    def get_style(self):
        return self.style

    def __str__(self):
        return "Car: {} {} {} Weight={:.2f} Fee=${:.2f}".format(
            self.get_license(), self.get_year(), self.get_style(),
            self.get_weight(), self.get_fee())


class Truck(Vehicle):
    def __init__(self, the_license, the_year, the_wheels):
        super().__init__(the_license, the_year)
        try:
            self.wheels = int(the_wheels)
        except ValueError:
            self.style = 0

    def set_weight(self, the_weight):
        super().set_weight(the_weight)
        if self.get_weight() < 3000:
            self.set_fee(40)
        elif self.get_weight() < 5000:
            self.set_fee(50)
        elif self.get_weight() < 10000:
            self.set_fee(60)
        else:
            self.set_fee(70)

    def get_wheels(self):
        return self.wheels

    def __str__(self):
        return "Truck: {} {} {} wheels Weight={:.2f} Fee=${:.2f}".format(
            self.get_license(), self.get_year(), self.get_wheels(),
            self.get_weight(), self.get_fee())


class Motorbike(Vehicle):
    def __init__(self, the_license, the_year):
        super().__init__(the_license, the_year)
        self.cc = 0

    def set_CC(self, cc):
        try:
            self.cc = int(cc)
        except ValueError:
            self.cc = 0
        if self.get_CC() < 50:
            self.set_fee(10)
        elif self.get_CC() < 200:
            self.set_fee(20)
        else:
            self.set_fee(35)

    def get_CC(self):
        return self.cc

    def __str__(self):
        return "Motorbike: {} {} {} cc Fee=${:.2f}".format(
            self.get_license(), self.get_year(), self.get_CC(), self.get_fee())


def main():
    # Create some vehicles
    v1 = Vehicle("AB 123", 2010)
    c1 = Car("SF 735", 2007, "Station")
    t1 = Truck("TU 765", 1994, 6)
    b1 = Motorbike("XY 666", 2005)
    c1.set_weight(3500)
    t1.set_weight(9000)
    b1.set_CC(250)
    # Print info
    print(v1)
    print(c1)
    print("The weight of the car is: {:.2f}".format(c1.get_weight() ))
    print(t1)
    print("The fee for the truck is: {:.2f}".format(t1.get_fee() ))
    print(b1)
    print("The CC of the bike is: {:.2f}".format(b1.get_CC() ))
    print()
    # Put the four vehicles into a list.
    # Then loop through the list and call the print function for each of the
    # vehicles.
    # You have to implement this part of the main program!
    # YOUR CODE GOES HERE
    my_vehicle_list = [v1, c1, t1, b1]
    for a_vehicle in my_vehicle_list:
        print(a_vehicle)

    v1 = c1
    print(v1)
    print()
main()
