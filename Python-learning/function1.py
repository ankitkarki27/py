print("If you want to convert nepali rupees to usd press 1 ")
print("If you want to convert usd to nepali rupees press 2 ")


def  nepalitousd(i):
       print(f"The conversion is{i/134}$")
def  usdtonepali(i):
       print(f"The conversion is Rs.{i * 134}")
a = int(input("Enter a number between 1 and 2: "))
if  a==1:
     b=int(input("Enter nepalese rupees amount to convert to usd "))
     nepalitousd(b)
elif  a==2:
     c=int(input("Enter usd amount to convert in nepali rupees "))
     usdtonepali(c)
else:
    print("Invalid Input")






