# method overloding

class math:
    def add(self,a,b,c):
        return a+b+c
    
m1=math()
# print(m1.add(100))
# print(m1.add(10,20))
print(m1.add(10,20,30))

# method overriding
class car:
    def colur(self):
        print("colour of this car is blue")

class bike(car):
    def colur(self):
        print("clour  of this bike is black")

b1=bike()
b1.colur()