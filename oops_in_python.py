"""class person:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("hello,my name is",self.name)
person_1=person("shwetank")
person_1.speak()
def __init__(self,name):
        self.name=name"""
#Inheritance in python
# Base class (Parent)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(self.brand + " " + self.model + "'s engine started.")

    def stop_engine(self):
        print(self.brand + " " + self.model + "'s engine stopped.")

# Derived class (Child)
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def honk(self):
        print(self.brand + " " + self.model + " says: Beep Beep!")

    def start_engine(self):
        print(self.brand + " " + self.model + " is a " + self.fuel_type + " car.")
        super().start_engine()

# Another derived class
class Motorcycle(Vehicle):
    def kick_start(self):
        print(self.brand + " " + self.model + " is being kick-started!")

# Usage
my_car = Car("Toyota", "Camry", "Petrol")
my_bike = Motorcycle("Honda", "CBR")

my_car.start_engine()
my_car.honk()
my_car.stop_engine()

print("-----")

my_bike.start_engine()
my_bike.kick_start()
my_bike.stop_engine()
