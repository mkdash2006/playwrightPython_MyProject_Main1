# Constructor - one speacial type of function
# Constructor is defined as __init__(self) and can be used inside class.
# Constructor automatically called when an object (instances of that class) is created outside.
# Constructor are 2 types: Default Constructor, Parameterize Constructor.

# Default Constructor......................
#"""
class car:
    def __init__(self):
        self.brand = "Tata"  # Attribute or Variable
        self.model = "Safari"  # Attribute or Variable
        print("Constructor Called with Default values")

obj1=car()  # output: Constructor Called
print("Default Constrictor:") # output: Default Constrictor:
print("Object Created:", obj1)
print("Car Brand:", obj1.brand)  # output: Tata
print("Car Model:", obj1.model)  # output: Safari
# Called the values what default used in constructor
#"""
#-------------------------------------------------
# Parameterize Constructor
# class car2:
#     def __init__(self, brand, model):
#         self.brand = "Tata"
#         self.model = "Safari"
#         print ("Constructor Called with Parametrize values")

# obj2 = car2("Kia", "Seltos")
# print("Parameterized Constrictor:") # output: Parameterized Constrictor:

# print("Car Brand:", obj2.brand)  # output: Kia
# print("Car Model:", obj2.model)  # output: Seltus