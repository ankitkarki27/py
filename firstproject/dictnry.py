my_dict = {
    "name": "ankit",
    "address": "bkt",
    "age": 23,
    "college": "RRBCA"
}
print(my_dict)

# Get user input
# key = input("Enter a key (name, address, age, college,email): ")

# Print the value associated with the given key
# Using my_dict.get(key) will return None if the key is not found, instead of raising a KeyError
# print(my_dict.get(key, "Key not found"))

# adding and updating element
my_dict["email"]="abc@gmail.com"
my_dict["age"]=24

# print(my_dict)

# key = input("Enter a key (name, address, age, college,email): ")
# print(my_dict.get(key, "Key not found"))

# removing

del my_dict["age"]
print(my_dict)
# pop deletes the last added item
my_dict.popitem()
print(my_dict)

# Dictionary methods
marks = {
        "ram":80,
        "sita":90,
        "Hari":89,
        "gyan":77
}
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"gyan":88,"ankit":100})
print(marks)

# get m,ethod

