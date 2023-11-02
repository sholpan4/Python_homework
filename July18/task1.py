class Animal:
    def _init_(self, name, weight, size):
        self.name = name
        self.weight = weight
        self.size = size

    def talk(self):
        print("Mmmmmmm...")

    def eat(self, meal):
        self.size += len(meal)
        self.weight += len(meal)

class Herbivore(Animal):
    def _init_(self, name, weight, size, ratio):
        super()._init_(name, weight, size)
        self.ratio = ratio

    def eat(self, meal):
        if meal in self.ratio:
            super().eat(meal)
        else:
            print(f"{self.name} не ест {meal}.")

class Predator(Animal):
    def _init_(self, name, weight, size):
        super()._init_(name, weight, size)
        self.prey_eaten = set()

    def eat(self, meal):
        if meal not in self.prey_eaten and meal.weight < self.weight and meal.size < self.size:
            super().eat(meal.name)
            self.size += 0.2 * meal.size
            self.weight += 0.2 * meal.weight
            self.prey_eaten.add(meal)
        else:
            print(f"{self.name} не может съесть {meal.name}.")

class Goose(Herbivore):
    def _init_(self, name, weight, size):
        super()._init_(name, weight, size, ["grass"])
        self.voice = "Honk"

    def talk(self):
        print(f"{self.name} says '{self.voice}'")

    def fly(self):
        print(f"{self.name} is flying.")

class Wolf(Predator):
    def _init_(self, name, weight, size):
        super()._init_(name, weight, size)
        self.voice = "Howl"

    def talk(self):
        print(f"{self.name} says '{self.voice}'")

    def hunt(self):
        print(f"{self.name} is hunting.")

goose1 = Goose("Goose 1", 10, 1)
goose2 = Goose("Goose 2", 9, 0.9)

wolf1 = Wolf("Wolf 1", 20, 2)
wolf2 = Wolf("Wolf 2", 18, 1.8)