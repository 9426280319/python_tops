# Q9: Python programs to demonstrate different types of inheritance
# single inheritance
class car:
    def colur(self):
        print("this car color is blue")

class bike(car):
    def design(self):
        print("this bike design is black")

b1=bike()
b1.colur()
b1.design()


#multiple inheritance

class car:
    def colur(self):
        print("this car color is blue")

class truck:
    def pattern(self):
        print("this is a truck pattern")

class bike(car,truck):
    def design(self):
        print("this bike design is black")

b1=bike()
b1.colur()
b1.design()
b1.pattern()


# multi-level inheritance
class car:
    def colur(self):
        print("this car color is blue")

class truck(car):
    def pattern(self):
        print("this is a truck pattern")

class bike(truck):
    def design(self):
        print("this bike design is black")

b1=bike()
b1.colur()
b1.design()
b1.pattern()
