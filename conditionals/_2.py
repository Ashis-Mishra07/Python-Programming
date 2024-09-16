day=input("Enter the day")
age=input("Enter ur age")
age=int(age)

if day=="Wednesday":
    if(age>=18):
        print("Today is Wed , get a discounted price of $2 so Pay $16")
    else:
        print("Today is Wed , get a discounted price of $2 so Pay $6")
else:
    if(age>=18):
        print("Pay $18")
    else:
        print("Pay $8")
