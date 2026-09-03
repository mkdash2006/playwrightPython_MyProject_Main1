# dict is a collection of key-value pairs, where each key is unique and maps to a specific value. 
# Dictionaries are mutable, meaning you can change their contents after creation. 
# They are unordered in versions of Python before 3.7, but from Python 3.7 onwards, 
# they maintain insertion order.

# student = ["manoj", 70, 70, 90]
student = {
    "name": "Manoj",
    "maths": 70,
    "science": 70,
    "english": 90
}
print (student ["maths"])  # Accessing value using key
print (student.get("maths"))  # Accessing value using get() method
# print (student.add("Python": 90))  # Adding a new key-value pair
student ["python"] = 85
print (student)
#student.update({"python": 95})  # Updating an existing key-value pair
#print (student)

#print (student.update({"python": 100}) or student)
# print ({** student, "python": 99})  # Updating an existing key-value pair using dictionary unpacking
student.update({"python1": [91, 92, 93], "python2": [94, 95, 96]})  # Updating multiple key-value pairs
print (student)       
#student1 = student ["python1"][1]  # Accessing a specific value from a list within the dictionary
#print (student1)
#print(student["python2"][2])  # Accessing a specific value from a list within the dictionary
#print(student.keys())  # Getting all the keys in the dictionary
#print(list(student.keys()))  # Getting all the keys in the dictionary as a list
#print(student.values())  # Getting all the values in the dictionary
student.pop("python1")  # Removing a key-value pair using pop() method
print(student)
student.popitem()
print(student)  # Removing the last inserted key-value pair using popitem() method