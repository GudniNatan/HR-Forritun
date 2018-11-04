import random


class Island(object):
    def __init__(self, size, prey_count=0, predator_count=0):
        self.gird_size = size
        self.grid = [[None for b in range(size)] for a in range(size)]
        self.init_animals(prey_count, predator_count)

    def __str__(self):
        rows = list()
        for row_num in range(self.gird_size-1, -1, -1):
            column_string = ""
            for col_num in range(self.gird_size):
                if self.grid[row_num][col_num]:
                    animal_str = str(self.grid[row_num][col_num])
                    column_string += "{:<2}".format(animal_str) + " "
                else:
                    column_string += "{:<2}".format(".") + " "
            rows.append(column_string)
        return "\n".join(rows)

    def addAnimal(self, animal):
        x, y = animal.x, animal.y
        self.grid[x][y] = animal

    def animal(self, x, y):
        if 0 <= x < self.gird_size and 0 <= y < self.gird_size:
            return self.grid[x][y]
        else:
            return -1

    def remove(self, animal):
        x = animal.x
        y = animal.y
        if self.grid[x][y] == animal:
            self.grid[x][y] = None

    def getRandomFreeSpot(self):
        x = random.randint(0, self.gird_size - 1)
        y = random.randint(0, self.gird_size - 1)
        while self.animal(x, y):
            x = random.randint(0, self.gird_size - 1)
            y = random.randint(0, self.gird_size - 1)
        return (x, y)

    def init_animals(self, prey_count=0, predator_count=0):
        for _ in range(prey_count):
            x, y = self.getRandomFreeSpot()
            prey = Prey(self, x, y)
            self.addAnimal(prey)
        for _ in range(predator_count):
            x, y = self.getRandomFreeSpot()
            prey = Predator(self, x, y)
            self.addAnimal(prey)


class Animal(object):
    def __init__(self, island, x=0, y=0, name="A"):
        self.island = island
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return self.name

    def move(self):
        """Move to an open, neighboring position ."""
        # neighbor offsets
        offset = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if not (i == j == 0)]
        random.shuffle(offset)
        for i in range(len(offset)):
            x = self.x + offset[i][0]  # neighboring coordinates
            y = self.y + offset[i][1]
            if not self.island.animal(x, y):  # neighboring spot is open
                self.island.remove(self)
                self.x, self.y = x, y
                self.island.addAnimal(self)
                break

    def breed(self):
        if self.breed_time == 0:
            offset = [(self.x + i,  self.y + j) for i in range(-1, 2) for j in range(-1, 2) if not (i == j == 0)]
            for space in offset:
                animal = self.island.animal(space[0], space[1])
                if not animal:
                    offspring = type(self)(self.island, x=space[0], y=space[1])
                    self.island.addAnimal(offspring)
                    self.starve_time = Predator.starve_time
                    self.breed_time = type(self).breed_time
                    break
        self.breed_time -= 1


class Predator(Animal):
    def __init__(self, island, x=0, y=0, name='R'):
        super().__init__(island, x, y, name)

    def eat(self):
        offset = [(self.x + i,  self.y + j) for i in range(-1, 2) for j in range(-1, 2) if not (i == j == 0)]
        for space in offset:
            animal = self.island.animal(space[0], space[1])
            if isinstance(animal, Prey):
                self.island.remove(self)
                self.x = animal.x
                self.y = animal.y
                self.island.addAnimal(self)
                self.starve_time = Predator.starve_time 
                break
        else:
            self.starve_time -= 1
        if self.starve_time == 0:
            self.island.remove(self)
            return


class Prey(Animal):
    def __init__(self, island, x=0, y=0, name='B'):
        super().__init__(island, x, y, name)


def main(predator_breed_time, predator_starve_time, initial_predators,
         prey_breed_time, initial_prey, size, ticks):
    Predator.breed_time = predator_breed_time
    Predator.starve_time = predator_starve_time
    Prey.breed_time = prey_breed_time
    tenerife = Island(size, initial_prey, initial_predators)
    for _ in range(ticks):
        print(tenerife, "\n")
        for x in range(tenerife.gird_size):
            for y in range(tenerife.gird_size):
                animal = tenerife.animal(x, y)
                if animal:
                    if isinstance(animal, Predator):
                        animal.eat()
                    animal.move()
                    animal.breed()

main(6, 3, 10, 3, 50, 10, 100)
