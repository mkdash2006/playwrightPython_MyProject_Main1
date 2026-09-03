# Function - Reusable code block. it must return.
# Otherwise print/output is none
# Use a function when you need to perform a task & reuse multiple time.
# def f1():
#     biju = 3  # "biju" is a variable / local variable
#     c = biju       
#     return c

# print (f1())  

# Class - A class is the blueprint
# Objects (Instances)- and an object is the real thing created 
# from that blueprint. Each object has its own data but shares 
# the same structure and behaviors defined by the class.
# A class tells how something works.
# Inside class - attribute, function and constructor.
# function - Can exist anywhere, work when we manually call it (syntax 
#               def())
# Constructor - Must be inside a class, work automatically... 
                # ...when obj created  ) syntax same as function, def__init__()
                # Its job is to initialize attributes of the object.

# Using self in a class/function without constructor
"""
class firstclass():  
    biju = 3    # "biju" is a class attribute / class variable
    def f1():
        raju = 5
        print("Raju:", raju)
    def f2(self):
            self.manju = 8
            print("Manju", self.manju)
    def f3(self):
            self.anju = 4
            print("Anju", self.anju)
        
print ("Biju:", firstclass.biju) 
firstclass.f1()
obj1 = firstclass()
obj1.f2()
obj1.f3()
obj2 = firstclass()
obj1.f3()
"""
##########################  NOW WITH CONSTRUCTOR
class firstclass():
    biju = 3    # "biju" is a class attribute / class variable

    def __init__(self):
    self.b=6
    # pass

    def f1():
        raju = 5
        print("Raju:", raju)
    def f2(self):
            self.manju = 8
            print("Manju", self.manju)
    def f3(self):
            self.anju = 4
            print("Anju", self.anju)
        
print ("Biju:", firstclass.biju) 
firstclass.f1()
obj1 = firstclass()
obj1.f2()
obj1.f3()
obj2 = firstclass()
obj1.f3()
