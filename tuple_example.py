# Creating a list and a tuple
my_list = ["apple", "banana", "cherry"]
my_tuple = ("apple", "banana", "cherry")

print("List:", my_list)
print("Tuple:", my_tuple)

# Accessing elements
print("\nAccessing Elements:")
print("List[1]:", my_list[1])
print("Tuple[1]:", my_tuple[1])

# Mutability Test
print("\nMutability:")
my_list[1] = "grape"
print("Modified List:", my_list)

try:
    my_tuple[1] = "grape"
except TypeError as e:
    print("Error when modifying tuple:", e)

# Adding elements
print("\nAdding Elements:")
my_list.append("orange")
print("List after append:", my_list)

try:
    my_tuple.append("orange")
except AttributeError as e:
    print("Error when appending to tuple:", e)

# Length
print("\nLength:")
print("Length of list:", len(my_list))
print("Length of tuple:", len(my_tuple))

# Iteration
print("\nIteration:")
print("List elements:")
for item in my_list:
    print(item, end=" ")

print("\nTuple elements:")
for item in my_tuple:
    print(item, end=" ")

# Memory efficiency
my_list.pop()
print(" ")
print("List elements:")
for item in my_list:
    print(item, end=" ")
import sys
print("\n\nMemory Size:")
print("List memory size:", sys.getsizeof(my_list))
print("Tuple memory size:", sys.getsizeof(my_tuple))
