""" 
mylist = [1,2,3,4,6,7,5,6,7,3,2]
print ("mylist:", mylist)  
myset = set(mylist) 
print ("myset:", myset)
mytuple = tuple(myset)
print ("mytuple:", mytuple)
mytuple2 = tuple(mylist)
print ("mytuple2:", mytuple2)

newlist = [1,2,3,4,6,7,5,6,7,3,2]
newlist = set(newlist)
print ("newlist:", newlist)  """

s1 = [1,2,3,4, "true", "false", True, False,6,7]  
print(s1) 
s1 = {1,2,3,4, "true", "false", True, False,6,7}     
print(s1) 