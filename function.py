class Car:
    model = "BMW"
    engine = 1.6

a = Car.model
Car.colour = "red"
b = Car.colour
x = Car()
x.colour = 'blue'
x.model = 'IZH'
print(x.__dict__)
print(x.model,Car.model)