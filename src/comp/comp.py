# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':

print("Start with D")
a = [data.name for data in humans if data.name[0] == 'D' ]
print(a)
print("\n")

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [data.name for data in humans if data.name[-1] == 'e']
print(b, "\n")


# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = [data.name for data in humans if data.name[0] == 'C' or data.name[0] =='D' or data.name[0] =='E' or data.name[0] =='F' or data.name[0] =='G']
print(c, "\n")

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [data.age + 10 for data in humans ]
print(d, "\n")

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f"{data.name}-{data.age}" for data in humans]
print(e, "\n")

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [tuple((i) for i in (data.name, data.age)) for data in humans if data.age == 27 or data.age == 28 or data.age == 29 or data.age == 30 or data.age ==31 or data.age == 32]
print(f, "\n")

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.

# I FOUND THIS DIFFICULT
print("All names uppercase:")
import copy
g = copy.deepcopy(humans)
for i in g:
    i.name = (i.name.upper())
    i.age = (i.age + 5)
print(g, "\n")

print(humans)


# g = []

# new_list = copy.deepcopy(humans)
# for i in new_list:
#     i.name = (i.name.upper())
#     i.age = (i.age + 5)
#     g.append(i)
# print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [(math.sqrt(data.age)) for data in humans]
print(h)
