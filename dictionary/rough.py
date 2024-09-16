# Creating a dictionary
person = {
    "name": "Ashis",
    "age": 25,
    "city": "Bhubaneswar"
}

# Accessing elements
print(person["name"])  # Output: Ashis
print(person.get("age"))  # Output: 25

# print(person["namee"]) # Since key not found so it will return error
# print(person.get("agee"))  # Since key not found , it will return nothing , no error 

# Adding or updating elements
person["email"] = "ashis@example.com"
person["age"] = 26

print(person)


# Iterating through dictionary
for key in person:
    print(key, person[key])

for key,value in person.items():
    print(key,value)


# Checking if a key exists
if "name" in person:
    print("Name is present")


# Length of a dictionary
print(len(person))

# popping
person.popitem() # Removes the last inserted item
person.pop("name")

# Deleting elements
del person["city"] # this will remove form the reference 


# Copying a dictionary
person_copy = person.copy()

# Clearing a dictionary
person.clear()

print(person)  # Output: {}
print(person_copy)  # Output: {'name': 'Ashis', 'age': 26}


# nested Dictionary
data = {
    "name": "Ashis",
    "age": 25,
    "city": "Bhubaneswar",
    "education": {
        "degree": "B.Tech",
        "year": 2020
    }
}

print(data["age"])
print(data["education"])
print(data["education"]["degree"])


squared_num={x:x**2 for x in range(10)}
print(squared_num)

# Dictionary methods
keys = person.keys()
values = person.values()
items = person.items()

print(keys)  # Output: dict_keys(['name', 'age'])
print(values)  # Output: dict_values(['Ashis', 26])
print(items)  # Output: dict_items([('name', 'Ashis'), ('age', 26)])

default_value="Not Found"
# make dict with keys and default values
default_dict=dict.fromkeys(keys,default_value)
print(default_dict)
