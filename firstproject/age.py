from datetime import datetime
dob=input("enter your birth year:")
dob=int(dob)
cy=datetime.now().year #gives current year(cy)
age=cy-dob
if dob>cy:
    print("enter correct birth year")
else:
    print("your current age is "+str(age))
    