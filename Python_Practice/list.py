# LIST - List starts with square brackets [] and can hold multiple values of different data types.
# Collections, Mutable, Ordered, Duplication Allowed.

b2 = [10, 20, "Manoj", 10, "b", "Python", "Java", "C++"]
print(b2)
print("Memory Address id:", id(b2))
#Append - add one string at the end of the list
b2.append("Favorite") 
print("Appended single Value:", b2)
#Extend - add multiple strings at the end of the list
b2.extend (["Language", "is", "a", "programming", "language"])    
print("Extended multiple Values:", b2)   
b2 += ["$100", "$200", "$300", "$400", "$500"]
print("Extended multiple Values:", b2)  
print("Memory Address id:", id(b2))
# DELETE LIST BY INDEX
b2.pop ()  # remove the first occurrence of the specified value
print(b2)   
b2.pop(3)  # remove the first occurrence of the specified value
print(b2)
# DELETE LIST BY VALUE
b2.remove("Java")
print(b2)
# CLEAR - REMOVE ALL THE ELEMENTS FROM THE EXISTING LIST 
b2.clear()
print("All the List Values are Cleared:", b2) 
print("Memory Address id:", id(b2))     
b2 += ["$100", "$200", "$300", "$400", "$500"]    
print(b2) 
print("Memory Address id:", id(b2))
# EMPTY - REMOVE THE LIST FROM MEMORY
b2 = []  # empty the list
print("List removed from the Memory:", b2)
print("New Memory Address id:", id(b2))