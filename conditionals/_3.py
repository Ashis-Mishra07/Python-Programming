year=input("Enter the year")
year=int(year)

if year%400==0  or year%4==0 and year%100!=0:
    print("Leap year")   
else:
    print("Not aLeap year")



