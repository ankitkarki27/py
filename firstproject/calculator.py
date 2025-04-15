# calculator
num1=float(input("first num:"))
num2=float(input("second num:"))

print(" press 1 for add\n press 2 for sub\n press 3 for mul\n press 4 for div")

choice=int( input ("enter your choice 1-4:"))

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2)

else:
    print("invalid input")

