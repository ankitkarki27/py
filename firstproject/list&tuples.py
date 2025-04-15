# List

# 1. List Slicing and Advanced Operations
# List slicing allows you to access sub-parts of a list using the syntax list[start:stop:step].
# This is a powerful tool for manipulating lists efficiently.

# Example:
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::2])

# 2.Advanced list Comprehensions
#list comprehensions can include nested loops and conditional logic to create complex lists.
#in a readable adn concise manner.

matrix=[[1,2,3],[4,5,6],[7,8,9]]
flattened = [num for row in matrix for num in row ]
print(flattened)
