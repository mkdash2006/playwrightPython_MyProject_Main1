# SET - Set starts with curly brackets {} and can hold multiple values of different data types.
# Collections, Mutable, UnOrdered, Duplication Not Allowed.

b1 = {10, 20, "Manoj", 10, "b", "Python", "Java", "C++", "Python", "Python"}
print(b1)
#b1.append("Python1")  # This will raise an AttributeError since sets do not have an 'append' method
b1.add("Python2")
print(b1)
b1.update(["Language", "is", "a"])  # This will add multiple elements to the set
print(b1)
#print(b1[1:4])  # This will raise a TypeError since sets do not support indexing or slicing
b1.remove("b")  # This will remove the element "Python" from the set
print(b1)
# b1.pop(2)  # This will remove and return an arbitrary element from the set,bcoz sets are unordered.
