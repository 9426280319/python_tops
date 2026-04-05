def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        print("number not devide by 0")
    return a/b

def mod(a,b):
    return a%b


num1=float(input(f"enter first number:-"))
num2=float(input(f"enter first number:-"))

print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.diverstion")
print("5.modul")
choise=int(input("enter your choise(1/2/3/4/5):"))


if choise == 1:
   print(add(num1,num2))
elif choise == 2 :
    print(sub(num1,num2))
elif choise == 3:
   print( mul(num1,num2))
elif choise == 4:
   print( div(num1,num2))
elif choise == 5 :
    print(mod(num1,num2))



