# super() used in a child class to call a method from a parent class
class shape:
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled
    def discrip(self):
        print(f'this is {self.color} and {'filled' if self.filled else 'not filled'}')

class circle(shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius=radius
    
class square(shape):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.width=width

class triangle(shape):
    def __init__(self,color,filled,width,height):
        super().__init__(color,filled)
        self.height=height
        self.width=width

circle=circle('red',True,50)
print(circle.color)
print(circle.filled)
print(f'{circle.radius}cm')


circle.discrip()   ##from parent class