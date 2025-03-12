class animal:
    def __init__(self, name, food):
        self.name=name
        self.food=food
    def __str__(self):
        return f"{self.name} eats {self.food} every day"

a1=animal("Cow", "grass")

class neighboor(animal):
    def __init__(self, name, food, ability):
        super().__init__(name, food)
        self.ability=ability
    def fly(self, ability):
        return f"{self.name} can {self.ability}"
    def __str__(self):
        return f"{self.name} eats {self.food}  and can {self.ability} every day"
a2=neighboor("Eagle", "meat", 'fly')

class neighboor(animal):
    def __init__(self, name, food, ability):
        super().__init__(name, food)
        self.ability=ability
    def __str__(self):
        return f"{self.name} eats {self.food} and can {self.ability} every day"
a3=neighboor("Fish", "small fish", "swim")

class neighboor(animal):
    def __init__(self, name, food, activity):
        super().__init__(name, food)
        self.activity=activity
    def __str__(self):
        return f"{self.name} eats {self.food} and do {self.activity} every day"
    def do(self, activity):
        return f"{self.name} does {self.activity}"
a4=neighboor("Dog", "meat", "bark")


print(a1)
print(a2)
print(a3)
print(a4)