# Control Flow
# 1. complex conditions
# Complex conditions involve combining multiple conditions using logical operators
# (and, or, not).
# In the example below, the condition checks if x is greater than 10 and
# either less than 20 or an even number.

x=10
if x>10 and (x <20 or x%2==0):
    # Check if x is greater than 10. check if either x is less  than 20 or x is an even number.
    print("met")
else:
    print("not met")

# 2.Nested if else statements

x=20
if x>10:
    print("x greater than 10")
    if x<15:
        print("x is between 10 and 15")
    else:
        print("x is 15 or greater than 15")
else:
    print(" x is 10 or less ")



# 3. Switch-Case Statements (Using Dictionaries or match-case)
# Python doesn't have a native switch-case statement, but you can simulate it using dictionaries
# or match-case introduced in Python 3.10.
# These methods provide a way to handle multiple conditional branches more cleanly
# than multiple if-elif-else statements.

#using dictionaries

def switch(case):
    switcher = {
    #     here switcher is the  dictionary where
    # 1 maps to one,2 maps to two,3 to three and 4 to four...
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        # 5:"five"
    }
    return switcher.get(case,"Invalid case")

# print(switch(1))
# print(switch(2))
# print(switch(5))


#using match-case(Python 3.10+):
def match_case_ex(x):
    match x:
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case 4:
            return "four"
        case _:
            return "Invalid case"
    # Calling the function and printing the results
print(match_case_ex(1))  # Output: "one"
print(match_case_ex(2))  # Output: "two"
print(match_case_ex(5))  # Output: "Invalid case"


#FUNCTIONS
# 1. Function Arguments
#keyword arguments
# ANS:Keywords arguments allow us to specify default values and provide arguments by name,making the function call more readable.
# def function_name(parameters):
#     here def means keywords used to declare a function
# function body
#     # code to execute
#     return result

def greet(name,greeting ="hello"):
    return f"{greeting},{name}!"

print(greet("ram"))
print(greet("sita","Hi"))

# example 2
def area(l,b):
    return l*b

print(area(2,5))
print(area(1.2,5))

# *args and **kwargs:
# The *args and **kwargs syntax is used to handle a variable number of positional and keyword arguments respectively.

# *args allows the function to accept any number of positional arguments as a tuple.
# **kwargs allows the function to accept any number of keyword arguments as a dictionary.

# display_info(1, 2, 3, name="Alice", age=25)
# display_info(1, 2, 3, name="Alice", age=25): Calls the function with three positional arguments (1, 2, 3) and two keyword arguments (name="Alice" and age=25).

def display_info(*args,**kwargs):
    print("Args:",args)
    print("Kwargs:",kwargs)

display_info(1,2,3,name="hari",age="24")

# combining args with a function
# it allows us to pass a variable number of arguments to a function.
# this is useful when we don't know how many arguments will be passed to your funcn

def sum(*args):
    total=0
    for num in args:
        total += num
        # For each num, the loop adds num to total.
    return total

# calling the funcn with different numbers of arguments
print(sum(10,20,30,40))
print(sum(5))
print(sum())

## combining **kwargs with a function

def display_info(**kwargs):
    for key,value in kwargs.items():
        print (f"{key}:{value}")

display_info(brand="CG",model="CG123",year=2020)

#2. Lambda Functions
#Lambda functions are small anonymous functions defined using the lambda keyword.
# They are typically used for short, throwaway functions.
#example

add = lambda x, y:x+y
print(add(2,3))

#3 High order functions

#high order functions are the functions that take other functions as arguments or return them.
#commonexamples includes map,filter and reduce which apply a function to all items in an iterable,filter items based on a condn and reduce a list tio a single value respectively.

#1.map
# Example 1: Lambda Function with map
# Using map to apply a lambda function to a list of values:
# squiares of each number in the list
n=[1,2,3,4,5,6,7,8,9]
squares= map(lambda x:x **2, n)
print(list(squares))

#2 Filter
evens=filter(lambda x: x % 2== 0,n)
print(list(evens))

odds=filter(lambda x: x % 2!= 0,n)
print(list(odds))

#reduce
# Importing the reduce function from the functools module
from functools import reduce
sum=reduce(lambda x,y:x+y,n)
print(sum)
# 45
# The final result is the sum of all elements in the numbers list.

