# class variable is shared among all instance of a class,its outside the constructs.

class student:
    class_year=2025       #it will be shared across whole class with same value
    no_students=0
    def __init__(self,name,age):
        self.name=name
        self.age=age 
        student.no_students+=1                  #need to call bby the class so it increment everytime.

stu1=student('Tom',20)
stu2=student('jerry',15)

print(stu1.name) #Tom
print(stu1.age) #20
print(stu1.class_year)  #shared-variable 2025

print(stu2.name) #jerry
print(stu2.age) #15
print(stu1.class_year)    #shared-variable 2025

print(student.no_students)   # its should be 2 as there are 2 students

print(f'my class of {student.class_year} has {student.no_students} students.')