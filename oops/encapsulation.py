class Car:
    def __init__(self , brand , model):
        self.__brand=brand
        self.model=model

    def get_brand(self):
        return self.__brand
    
    def full_name(self):
        return f"{self.__brand} {self.model}"

myCar=Car("Toyota","Corolla")
print(myCar.__brand)
print(myCar.get_brand())


# note : __paramter make the parameter as private , so it will not be accessible outside the class
# unless we have to make getter and setter for it 


#make some setter for it 
class Car:
    def __init__(self , brand , model):
        self.__brand=brand
        self.model=model

    def get_brand(self):
        return self.__brand
    
    def set_brand(self,brand):
        self.__brand=brand
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
myCar=Car("Toyota","Corolla")
print(myCar.get_brand())
myCar.set_brand("Honda")
print(myCar.get_brand())



