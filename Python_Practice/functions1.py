# Functions - For Repeatative steps in multiple place, Its a block of code 
# execute based on our preference. Util unless we called it, it will not run.
# Defince a function

# a=1
# b=2
# c= a + b
# print (c)
##################################
# def sum():
#     a=1
#     b=2
#     c=a+b
#     print(c)

# sum()
####################################### Hard corded variable value changed, remaing same in the function
# def sum1():
#     a=3
#     b=4
#     c=a+b
#     print (c)
# sum1()
   ####################################### Instead of hard coding, use function parameter
# def sum2(a,b):    # ---------- a,b is the parameter passed
#     c=a+b
#     print(c)

# sum2(4,5)         # ----------- 4,5 is the arguments
#################################### Passed parameter values
# def sum3(a=2,b=3):
#     c=a+b
#     print(c)

# sum3() 
################################# parameter value overwritten with arguments value
# def sum4(a=2,b=3):
#     c=a+b
#     print(c)

# sum4(6,5)
###################################### Return variable result, or return any variable/value
# def m1():
#     a=2
#     b=2
#     c=a+b
#     return c
# print(m1())
###################################### Return variable result, or return any variable/value
def mk1(a=2,b=2):
    c=a+b
    return c
#print(mk1())   
#print(mk1())
#print(mk1(4,6)) 
###########################
# def m2(a=2,b=8):
#     c=a+b
#     #return c
#     print(c)

# print(m2())
# #print(m2(6,6)) 
############################

