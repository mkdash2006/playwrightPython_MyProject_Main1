# TUPLE - Tuple starts with parentheses () and is immutable, meaning its elements 
# Cannot be changed after creation but can be replaced with a new Tuple.
# Collections, Immutable, Ordered, Duplication Allowed.

b1 = (10, 20, "Manoj", 10, "b", "Python", "Java", "C++", "Python", "Python")
# b1.add("Python1")  # This will raise an AttributeError since tuples do not have an 'add' method
print(b1)
# b1.append("Python2")  # This will also raise an AttributeError since tuples do not have an 'append' method
# b1.extend(["Language", "is", "a"])  # This will raise an AttributeError since tuples do not have an 'extend' method
# print(b1[2])  # Accessing the third element of the tuple
# print(b1[:])  # Accessing a slice of the tuple 
# print(b1[1:5]-1)  # Accessing a slice of the tuple from index 2 to 4
print("Length of this Tuple is:", len(b1))  # Getting the length of the tuple
print(f"Total count of {b1[5]} is: {b1.count('Python')}")  # Counting the occurrences of the value "Python" in the tuple
print(f"Index value of {b1[6]} is: {b1.index('Java')} position")   # Getting the index of the first occurrence of "Manoj " in the tuple
print(b1[1:-4])