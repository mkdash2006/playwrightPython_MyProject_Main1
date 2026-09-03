# from functions import mk1
# print ("Total Value:", mk1(6,6))

################################  original function in a sub folder...functions1a\fun1a.py

# from functions1a.fun1a import *
# print(mk1())
# #print ("Total Value:", mk1(7,8))

###########################   function call from other projects
# import sys
# sys.path.append("..\\MyPythoneProject2")
# from calltest import mk6
# print ((mk6))   
################## Call function from different folder but under same Project
# from NewFunction.newfun1 import *
# print (mk7())  

############### for function with empty body, use class keyword
#######  in python empty body, IndentationError: expected an indented block
# def e1 ():
#     pass

# print (e1())      
#################### Calling a Class from other file
from myclass import firstclass

print ("Biju:", firstclass.biju) 
firstclass.f1()   
