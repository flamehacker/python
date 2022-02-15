class Cat:

    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

c = Cat(name="Sharik", age = 2, colour = 'red')
print(c.age)
c.colour = 'grey'
print(c.colour)