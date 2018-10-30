class Vehicle(object):
    def __init__(self, the_license, the_year):
        try:
            self.license = str(the_license)
        except ValueError:
            self.license = ""
        try:
            self.year = int(the_year)
        except:
            self.year = 0
        self.weight = 0
        self.fee = 0.0

    def getLicense(self):
        return self.license

    def getYear(self):
        return self.year

    def getWeight(self):
        return self.weight

    def getFee(self):
        return self.fee

    def setWeight(self, the_weight):
        try:
            self.weight = int(the_weight)
        except ValueError:
            self.weight = 0

    def setFee(self, the_fee):
        try:
            self.fee = float(the_fee)
        except ValueError:
            self.fee = 0.0

    def __str__(self):
        return "Vehicle: {}  {}  Weight={} Fee=${}".format(
            self.getLicense(), self.getYear(), self.getWeight(), self.getFee())


class Car(Vehicle):
    def __init__(self, the_license, the_year, the_style):
        super().__init__(the_license, the_year)
        try:
            self.style = str(the_style)
        except ValueError:
            self.style = ""

    def setWeight(self, the_weight):
        super().setWeight(the_weight)
        if self.weight < 3000:
            self.setFee(30)
        elif 3000 <= self.weight < 5000:
            self.setFee(40)
        else:
            self.setFee(50)

    def getStyle(self):
        return self.style

    def __str__(self):
        return "Car: {}  {}  {}  Weight={} Fee=${}".format(
            self.getLicense(), self.getYear(), self.getStyle(),
            self.getWeight(), self.getFee())


class Truck(Vehicle):
    def __init__(self, the_license, the_year, the_wheels):
        super().__init__(the_license, the_year)
        try:
            self.wheels = int(the_wheels)
        except ValueError:
            self.style = 0
