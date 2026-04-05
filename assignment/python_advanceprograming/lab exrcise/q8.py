# Q8: Python program to create a class and access its properties using an object

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("customer name is:-",self.name)
        print("customer age is:-",self.age)

s1=student("sneha",21)
s1.display()

