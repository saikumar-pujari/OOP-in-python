# inhertance allows class  to inherit attribute and method from another class

class animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True
    def sleep(self):
        print(f'{self.name} is sleeping')
    def walk(self):
        print(f'the {self.name} is walking')
class dog(animal):           #use the another classname and then use( ) and call the required class to inherit.
    pass
class cat(animal):
    pass
class mouse(animal):
    def speak(self):    # it can have it own function also.
        print(f'the {self.name} makes a sound mus mus mus')

dog=dog('scooby')
cat=cat('garfield')
mouse=mouse('micky')

print(dog.name) #scooby
dog.sleep() 
dog.walk()

print(cat.name) #garfield
cat.sleep()
cat.walk()

print(mouse.name) #micky
mouse.sleep()
mouse.walk()
mouse.speak() # it can have it own function also.


###############################################################################################################################################33
#----------------------multiple-inheritance----------------------------------------------------------
# eg---->c(b,a)-->(c-->b--->a)
class animal:
    def eat(self):
        print('this animal eats')
    def sleep(self):
        print('this animal also sleeps')
class prey(animal):
    def fly(self):
        print('they will fly of')
class predator(animal):
    def hunt(self):
        print('they will hunt it down')
class rabit(prey):
    pass
class hawk(predator):
    pass
class fish(prey,predator):
    pass

rabit=rabit()
hawk=hawk()
fish=fish()

rabit.fly()     #this will fly of
# rabit.hunt()   # this will show error cuz no attributes
rabit.eat()    # this animal eats

hawk.hunt()         #thwy will hunt it down
# hawk.fly()  # this will show the error cuz of no attributes
hawk.sleep()        #this animal also sleeps which will be inherited from class animal.

fish.fly()
fish.hunt()