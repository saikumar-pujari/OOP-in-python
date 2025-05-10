# object is a bundle of related attribute(variables) and method(function).
# you need a class to create many object
#class is a (BLUEPRINT) to create the structure objects.

class car:
        def __init__(self,model,year,color,for_sale):           #we can assign any parameter to the function.
                self.model=model   #to acces the element need to call them using the self.
                self.year=year
                self.color=color
                self.for_sale=for_sale

car1=car('mustang',2024,'red',False)

print(car1) # it gives the memory addres for the class
print(car1.model)#need to use attribute acces model ( . ) befor calling it.
print(car1.year)
print(car1.color)
print(car1.color)
print(car1.for_sale)

car2=car('swify',2025,'blue',True)
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

###################Import a class##################
# to import a class from other location use this format
'''
 (from filename import classname)
'''

# -------------------------------------------------------------------------------------------------
class item:
    # pass   always printd True.
        def calculate_total_price(self,x,y): #self means it calls itself.
                return x*y

item1=item()
item1.name='phone'
item1.price=500
item1.quantity=5
item1.calculate_total_price(item1.price,item1.quantity)

#########create instances#######

print(type(item1)) #item
print(type(item1.name)) #str
print(type(item1.price)) #int
print(type(item1.quantity)) #int
print(type(item1.calculate_total_price)) #Method
print(item1.calculate_total_price(item1.price,item1.quantity)) #its a method.

#######Create a method #########
# methods are the action that objects perform.
random_str='aaaa'
print(random_str.upper())  #method use brackets at end unlike instances in item(above). 

#################acces the method##########
class car1:
        def __init__(self,name,year):
                self.name=name
                self.year=year
        
        def start(self):
                print(f'the car is starting the engine of {self.name} ')
        def stop(self):
                print(f'the car {self.name} has stoped')
        def describe(self):
                print(f'{self.name}\t{self.year}')

cada=car1('rollsroyce',2022)
cada.start()
cada.stop()
cada.describe()