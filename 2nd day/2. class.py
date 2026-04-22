class Person:
    def __init__(self,name,age):
       self.name= name 
       self.age=age
    
    def great(self):
        return f"Hi,i'm {self.name} and I'm {self.age} years old"
    
    def __repr__(self):
       return f"Person(name={self.name!r},age={self.age!r})"

p1=Person("Alice",25) 
p2=Person("Bob",30) 

print(p1)    #person(name=alice,age=25)
print(p1.greet())    #Hi,i'm alice and i'm 25 years old.
print(p2.name,p2.age)