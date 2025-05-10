# polymorphism means many form
# 2 ways for ploymorphism 1)inheritance 2)duck typing

################inheritance#################
from abc import ABC,abstractmethod
class shape:
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class square(shape):
    def __init__(self,width):
        self.width=width
    def area(self):
        return self.width**2
class pizza(circle):              ##it can be from circle               
    def __init__(self,radius):
        super().__init__(radius)

shape=[circle(5),square(6),pizza(5)]

for shape in shape:
    print(f'{shape.area()}cm2')

######################duck-typing####################
class animal:
    alive=True
class dog(animal):
    def speak(self):
        print('barks')
class cat(animal):
    def speak(self):
        print("MEOW")
class car:
    alive=False
    def speak(self):
        print("HORN")
animalS=[cat(),dog(),car()]
for animal in animalS:
    animal.speak()
    print(animal.alive)