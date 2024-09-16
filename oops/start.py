class Car:
    def __init__(self , brand , model):
        self.brand=brand
        self.model=model
    
    def full_name(self):
        return f"{self.brand} {self.model}"

myCar=Car("Toyota","Corolla")
print(myCar.brand)
print(myCar.model)
print(myCar.full_name())


