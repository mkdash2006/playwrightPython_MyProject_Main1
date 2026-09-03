#  Create a collection with all datatypes (int, float, bool, str, complex, list, tuple, set, dictionary)

from os import name


mycollection = [10, 20.5, True, "Hello", 2 + 3j, [1, 2, 3], (4, 5, 6), {7, 8, 9}, {"name": "Manoj", "age": 30}]
print(mycollection)
# print (mycollection["name"])  # Accessing value using key
# print (mycollection.get("name"))  # Accessing value using get() method
# print (mycollection.keys())  # Getting all the keys in the dictionary as a list
# print (list(mycollection.keys()))  # Getting all the keys in the dictionary as a list
print (mycollection[3], mycollection[8]["name"])  # Accessing the dictionary within the collection