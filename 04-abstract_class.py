# abstract class cannot be instantiaited of its own;meant to be sub classed
#  need to import abstract base class (AKA ABC)
from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

# vehicle=vehicle()  #cant instantite abstract classs vehichcle without implemenation.
class car(vehicle):
    
    def go(self):
        print("you can go with the car")
    
    def stop(self):
        print('you can stop the car')

car=car()
car.go()                #you can go with the car.
car.stop()                  #you can stop the car

class boat(vehicle):
    def go(self):
        print("you can sail with your both")

# boat=boat()
# boat.go()     #it will give an error that it can be implementated without stop method.
              #when we use abstract it work as check list that both the method should be definied in childeren class



class motor(vehicle):
    def go(self):
        print("you can ride with your motorbike")
    def stop(self):
        print('you can should stop with your bike')

motor=motor()
motor.go()          #you can ride with your motorbike
motor.stop()            #you can should stop with your bike


