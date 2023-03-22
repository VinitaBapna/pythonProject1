"""
# 1 program === variable and printing

print("Hello World!")

name = "Vinita"
age = 37

name = "Rudra"
age = 1.10

is_adult = True # true will give error as python is case sensitive

print("name")
print(name)
print(age)


# 2 program === input string and concatenation.
# by default everything entered from keyboard is stored as string in python.

name = input("What is your name?")
print("Hello " + name)


# 3 program === type conversion

old_age = input("What is your age? ")
# new_age = old_age + 2 # type error as old_age is string type

new_age = int(old_age) + 2
print(new_age)

# type conversion in 4 types : int(), float(), str(), bool()
print(float(18))


# 4 program === print sum of two numbers === first example of program writing

first = input("Enter first number : ")
second = input("Enter second number : ")

sum = int(first) + int(second)
print(sum)
print("The sum is : " + str(sum))


# 5 program === Strings and Keywords - 'in'
name = "Tony Stark"

print(name.upper()) # doesn't convert original string
print(name)
print(name.replace("Tony Stark", "Ironman")) # doesn't convert original string
print(name)
print(name.replace('T','M'))
print(name.find('S'))   # returns index value if found else return -1 if not found
print(name.find('s'))
print(name.find("Stark"))
print("T" in name) # returns boolean value True/False

# 6 program === Arithmetic operators     + - * / %(modulus:reminder) **(power) //(removes decimal value after division)
print("Add : " + str(5 + 2))
print("Subtract : " + str(5 - 2))
print("Multiply : " + str(5 * 2))
print("Divide(decimal value return) : " + str(5 / 2))
print("Divide(integer value return) : " + str(5 // 2))
print("Modulo(reminder return) : " + str(5 % 2))
print("Power : " + str(5 ** 2))

i = 5
# i = i + 2
i += 2
print(i)

# operator precedence
result = 2 + 3 * 5
print(result)           # answer = 17
result = (2 + 3) * 5
print(result)           # answer = 25

# 7 program === Comparison operators     < > <= >= == !=
print(3 < 2)    # False
print(3 > 2)    # True
print(3 <= 2)   # False
print(3 >= 2)   # True
print(3 == 3)   # True
print(3 != 3)   # False
print(3 != 2)   # True

# 8 program === Logical Operators    or and not
print(2 > 3 or 2 > 1)   # True
print(2 > 3 and 2 > 1)   # False
print(not 2 > 3)   # True

# 9 program === if-else
age = int(input("What is your age? "))

if age >= 18:
    print("You are an adult.")
    print("You can vote.")
elif age < 18 and age > 10:
    print("You are a teenager.")
else:
    print("You are child.")

print("Thank You!")

# 10 Program === range() function
numbers = range(5)
print(numbers)

# 11 Program === Loops - while
i = 1
while i <= 5:
    print(i)
    i += 1      # i = i + 1

# 12 Program === star pattern 1
i = 1
while i <= 5:
    print(i * "*")
    i = i + 1

# 13 Program === star pattern 2
i = 4
while i >= 1:
    print(i * "*")
    i = i - 1

# 14 Program === Loops - for
for item in range(5):
    print(item + 1)

# 15 Program === List [] // Mutable
emp = [101, "Vinita", 37, "vinita.bapna9@gmail.com"]
print(emp)

marks = [95, 98, 97]
print(marks[0])     # 95
print(marks[-1])    # 97
# print(marks[-4])    # IndexError: list index out of range
print(marks[0:2])   # index 2 is not included

for score in marks:
    print(score)

print(len(marks))       # 5

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

marks.append(96)
print(marks)

marks.insert(0, 99)
print(marks)

print(99 in marks)      # True
print(93 in marks)      # False

# 16 Program === break and continue
students = ["ram", "shyam", "varah", "kalki", "vaman"]

for student in students:
    if student == "kalki":
        break;
    print(student)

for student in students:
    if student == "varah":
        continue;
    print(student)

# 17 Program === tuple () are used but not compulsory // Immutable
marks = (95, 98, 97, 97, 97)
# marks[0] = 99       # TypeError - 'tuple' object does not support item assignment
print(marks.count(97))  # 3
print(marks.index(97))  # 2

person = "ram", "sita", "shyam", "radha"
print(person)

# 18 Program === set {} // unordered, index value can not be considered, value stored in random pattern.
marks = {95, 98, 97, 97, 97}
print(marks)        # {97, 98, 95}
# print(marks[0])     # TypeError - 'set' object is not subscriptable.

for score in marks:
    print(score)

# 19 Program === dictonary {key:value} // Important
marks = {"english" : 95, "hindi" : 98}
print(marks["hindi"])
marks["maths"] = 96;
print(marks)
marks["maths"] = 99;
print(marks)

# 20 Program === Functions // 3 types- in-built, module, user-defined
# in-built functions === int(), str(), range(), min(), max()
# module functions # modules are files consisting several functions
import random
print(dir(random))

from math import sqrt
print(sqrt(16))
# user-defined functions
"""
def sum(a, b = 4):
    print(a + b)

sum(1, 2)
sum(1)
