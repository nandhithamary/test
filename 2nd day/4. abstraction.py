from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass

class defender(Car):
    def mileage(self):
        print("the mileage is 7  kmpl")

class diago(Car):
    def mileage (self):
        print("the mileage is 13 kmpl")

class pajero(Car):
    def mileage(self):
        print ("the mileage is 13 kmpl")

d=defender()
d.mileage()

i=diago()
i.mileage()

p=pajero()
p.mileage()