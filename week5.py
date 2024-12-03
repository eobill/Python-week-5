# Part 1: Design Your Own Class
class Superhero:
    def __init__(self, name, superpower, strength):
        self.name = name
        self.superpower = superpower
        self.strength = strength

    def introduce(self):
        return f"I am {self.name}, and I can {self.superpower} with a strength of {self.strength}!"

    def fight(self):
        return f"{self.name} fights with unmatched strength!"

# Inherited class: Villain
class Villain(Superhero):
    def __init__(self, name, superpower, strength, evil_plan):
        super().__init__(name, superpower, strength)
        self.__evil_plan = evil_plan  # Encapsulated attribute

    def reveal_plan(self):
        return f"{self.name} reveals their evil plan: {self.__evil_plan}"

    def fight(self):
        return f"{self.name} fights with cunning and chaos!"

# Testing Part 1
hero = Superhero("Captain Code", "manipulate code", 95)
villain = Villain("Bugzilla", "cause glitches", 85, "Crash all systems worldwide!")

print(hero.introduce())
print(hero.fight())
print(villain.introduce())
print(villain.reveal_plan())
print(villain.fight())

# Part 2: Polymorphism Challenge
class Car:
    def move(self):
        return "The car is driving 🚗."

class Plane:
    def move(self):
        return "The plane is flying ✈️."

class Boat:
    def move(self):
        return "The boat is sailing 🛥️."

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    print(vehicle.move())
