# Arithimatic Operators, Assignment Operators, Comparison Operators, Logical Operators, 
# Identity Operators, Membership Operators, Bitwise Operators.

# 1. Arithimatic Operator ###############################
# Arithimatic operators are used to perform mathematical operations between numeric values.
# The common arithmetic operators in Python include:
# Addition (+): Adds two numbers together.
# Subtraction (-): Subtracts one number from another.
# Multiplication (*): Multiplies two numbers.
# Division (/): Divides one number by another and returns a float.
# Floor Division (//): Divides one number by another and returns the largest integer less than or equal to the result.
# Modulus (%): Returns the remainder of the division of one number by another.
# Exponentiation (**): Raises one number to the power of another.
###########################
a = 12
b = 3
# print (a + b)   
# print (a - b)
# print (a * b)
# print (a / b) # Division
# print ( a % b) # Modulus or Reminder
# print (a // b) # Floor Division
# print (a ** b) # Exponentiation
# print (2 ** 3 ) # Exponentiation

# 2. Assignment Operators ####### Action performed then value store into aa variable.
a = 2
a = a+3
a +=3

# 3. Comparison Operators #######  >. <, >=, <=, ==, !=   #### boolean result (True or False).
# print (2>2)  # False
# print (2<2)  # False
# print (2>=2) # True
# print (2<=2) # True
# print (2==2) # True
# print (2!=2) # False

# 4. Logical Operators #######  and, or, not   #### boolean result (True or False).
# Any one False then result is False, All True then result is True.
# print (True and True)   # True
# print (True and False)  # False
# print (False and True)  # False
# print (False and False) # False
# print (True and True and False)
# print ( 2==2 or 2>2)
# print ( 2==2 and 2>2)
# print (not(True))
# print (not(False))  

# 5. Identify Operators - is, is not
b1 = [1, 2]
b2 = [1, 2]
# print (b1 is b2)
# print (b1 == b2)
# print (b1 is b1)
# print (b1 is not b1)

# 6. Membership Operator ###  in, not in
c2 = [1,2,3]
print (3 in c2)
print (3 not in c2)