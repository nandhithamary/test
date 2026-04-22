class Animal:
    def speak(self):
        print("animal speak")

class Dog (Animal):
    def speak(self):
        print("dog barks")

class Cat(Animal):
    def speak(self):
        print("cat meows")

a=Animal()
a.speak()

d=Dog()
d.speak()