class Car:
    def __init__(self , brand , model):
        self.brand=brand
        self.model=model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self , brand , model , battery):
        super().__init__(brand,model)
        self.battery=battery
    
    def full_name(self):
        return f"{self.brand} {self.model} {self.battery}"
    


myCar=Car("Toyota","Corolla")
myElectricCar=ElectricCar("Tesla","Model S","100kWh")
# myElectricCar2=ElectricCar("250kWh")
print(myCar.brand)
print(myCar.model)
print(myCar.full_name())



# isinstance to check where the class made is instance of the class

print(isinstance(myElectricCar,ElectricCar) )
print(isinstance(myElectricCar,Car) )



#multiple inheritance
class A:
    def classA(self):
        return "I am class A"

class B:
    def classB(self):
        return "I am class B"
    
class C(A,B):
    def classC(self):
        return "I am class C"
    
objC=C()
print(objC.classA())
print(objC.classB())
print(objC.classC())

