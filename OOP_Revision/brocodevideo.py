# object is an instance of a class 

# a class is a function describing what methods and attributes an object might have 

class Car: 
     # attributes describe what an object is or has 

     def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour 

     def drive(self): 
         print("This car is driving")

     def stop(self):
         print("This car is stopped")


car_1 = Car("Ford", "Fiesta", 2014, "Black")

print(car_1.make)
print(car_1.model)
print(car_1.colour)

car_1.drive()

class Lorry(Car):

    def __init__(self, make, model, year, colour, weight):
        super().__init__(make, model, year, colour)
        self.weight = weight

L = Lorry("Ford", "Fiesta", 2014, "Black", 250)