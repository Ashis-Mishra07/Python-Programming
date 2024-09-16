# Creating a tuple
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 2, 3, 4, 5)
tuple3 = ("abc", 34, True, 40, "male")

# Type
print(type(tuple1))

# Accessing elements
print(tuple1[0])  # Output: apple
print(tuple2[-1])  # Output: 5

# Slicing a tuple
print(tuple1[1:3])  # Output: ('banana', 'cherry')
print(tuple2[:3])  # Output: (1, 2, 3)

# Unpacking a tuple
fruit1, fruit2, fruit3 = tuple1
print(fruit1)  # Output: apple
print(fruit2)  # Output: banana
print(fruit3)  # Output: cherry

# Looping through a tuple
for item in tuple1:
    print(item)

# Checking if an item exists
if "banana" in tuple1:
    print("Banana is in the tuple")

# Tuple length
print(len(tuple1))  # Output: 3

# Concatenating tuples
tuple4 = tuple1 + tuple2
print(tuple4)  # Output: ('apple', 'banana', 'cherry', 1, 2, 3, 4, 5)

# Multiplying tuples
tuple5 = tuple1 * 2
print(tuple5)  # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# Nested tuples
nested_tuple = (tuple1, tuple2)
print(nested_tuple)  # Output: (('apple', 'banana', 'cherry'), (1, 2, 3, 4, 5))

# Tuple methods
print(tuple1.count("apple"))  # Output: 1
print(tuple1.index("banana"))  # Output: 1

# Converting a list to a tuple
list1 = [1, 2, 3, 4, 5]
tuple_from_list = tuple(list1)
print(tuple_from_list)  # Output: (1, 2, 3, 4, 5)

# Converting a tuple to a list
list_from_tuple = list(tuple1)
print(list_from_tuple)  # Output: ['apple', 'banana', 'cherry']

# Tuple comprehension (using generator expression)
squared_nums = tuple(x**2 for x in range(5))
print(squared_nums)  # Output: (0, 1, 4, 9, 16)

