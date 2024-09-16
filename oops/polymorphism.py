class Car:
    def __init__(self , brand , model):
        self.brand=brand
        self.model=model
    
    def full_name(self):
        return "Hello i m from car method"
    

class ElectricCar(Car):
    def __init__(self , brand , model , battery):
        super().__init__(brand,model)
        self.battery=battery
    
    # def full_name(self):
    #     return "Hello i m from electric car method"
    


myCar=Car("Toyota","Corolla")
myElectricCar=ElectricCar("Tesla","Model S","100kWh")

print(myCar.full_name())
print(myElectricCar.full_name())
