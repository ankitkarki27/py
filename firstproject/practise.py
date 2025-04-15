# 1. Basic Syntax and Variables
print("Hello, World!")  # Basic print statement

# name= input('What is your name? ')
# print("Hello "+name)

# Variables and Data Types
name = "Alice"  # String
age = 30  # Integer
height = 5.6  # Float
is_student = True  # Boolean

# name="Ram"
# age=20
is_boy=True

print(name.upper())
# Display
print(f"He is {name},of {age} years, and {is_boy}")


# Display variables
# print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")

# 2. Basic Operators
a = 10
b = 3.1
sum=a+b
print(sum)
x=10+3.1
print(type(x))
# a="5"
# b="5"
print(int(a) - int(b))
# values of a and b are on string not on integer so print value will be 55
print(a+b)
# Arithmetic Operators
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponent: {a ** b}")

# Comparison Operators
print(f"Is a equal to b? {a == b}")
print(f"Is a not equal to b? {a != b}")
print(f"Is a greater than b? {a > b}")
print(f"Is a less than b? {a < b}")

a=10
print(a)
account_balance=1000
print(account_balance)
b=5

print(f"Is a greater than b? {a>b}")

# Logical Operators
x = True
y = False
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

# 3. Strings
message = "Hello, Python!"
print(message.lower())
print(message.upper())
print(message.strip("!"))
print(message.split(", "))

console = "Ankit Karki"
print(console.upper())

# name=ram
print(f"Formatted string: {name} is {age} years old")

# 4. Control Flow
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

level = 10
if level < 12:
    print("you are in school")
else:
    print("you are in college")

x=20
if x>10:
    print("x is greater than 10")

# 5. Loops
# For loop
for i in range(5):
    print(f"Loop iteration {i}")

for i in range(6):
    print(f"Loop {i}")

a='python'
for i in a:
    print(i,end='')
print()

a=12
if a==11 or a > 10 and a< 12:
    print('yes')
else:
    print('no')

# While loop
count = 0
while count < 5:
    print(f"While loop iteration {count}")
    count += 1

# 6. Functions
def greet_user(username):
    return f"Hello, {username}!"

print(greet_user("Alice"))

def age(name):
    return f"Iam {name} yeasrs old"
print(age(20))

def name(age):
    return f"This is {age} Years old"
print(name(20))

# Function with default argument
def add_numbers(x, y=10):
    return x + y

print(add_numbers(5))
# inthis call only argument 5 is provided.so return x=5 and y=10

print(add_numbers(5, 15))
#here both x and y are provided so x=5,y=15 x+y=20


# Function with keyword arguments
def person(name, age, city="Unknown"):
    return f"{name} is {age} years old and lives in {city}."

print(person("ram", 25, "ktm"))
print(person("sita", 28))

print (person("hero",30,"Jhapa"))


# 7. Lists and Tuples
# Lists
fruits = ["apple", "banana", "cherry"]
# add
fruits.append("Mango")
# remove
fruits.remove("banana")
# access
print(fruits[0])
print(f"List of fruits: {fruits}")

# List comprehension
squares = [x ** 2 for x in range(5)]
print(f"Squares: {squares}")

# print()
cube = [x ** 3 for x in range(4)]
print(f"Cube: {cube}")



# Tuples
colors = ("red", "green", "blue")
print(colors[1])
print(f"Tuple of colors: {colors}")

# 8. Basic I/O
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")
print(f"Hello " +user_name)

# Putting it all together: A simple calculator
def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"

    print(f"Result: {result}")

calculator()
