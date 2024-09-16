import math

def stats(num):
    area=math.pi*num**2
    circumference=2*math.pi*num
    return area,circumference


a ,c =stats(6)
print("area is ",round(a,3))
print("circumference is ",c)
print(stats(4))