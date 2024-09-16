class Car:
    total_car=0
    def __init__(self , brand , model):
        self.brand=brand
        self.__model=model
        Car.total_car+=1  # this way use Car class method since it is obj independent
    
    # def full_name(self):
    #     return f"{self.brand} {self.model}"
    
    @staticmethod    # decorators
    def generalDesc():
        return "This is a car class"
    
    @property        # decorators , not allowing others to override the method once it is made 
    def model(self):
        return self.__model__
    


myCar=Car("Toyota","Corolla")

myCar2=Car("Honda","Civic")
myCar3=Car("Honda","Civic")
myCar4=Car("Honda","Civic")

print(Car.total_car)
print(myCar.generalDesc())

myCar.model="Civic"  # this will give error since model is read only
print(myCar.model)





