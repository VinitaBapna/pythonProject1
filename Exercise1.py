# exercise 1
firstName = "Tony"
lastName = "Stark"
age = 51
is_genius = True

# exercise 2
superhero_name = input("What is your superhero name? ")
print(superhero_name)

# exercise 3 Mini Project - Calculator
first = int(input("Enter first number : "))
second = int(input("Enter second number : "))
operator = input("Enter operator (+,-,*,/,%) : ")

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid operator")
