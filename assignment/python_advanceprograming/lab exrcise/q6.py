# Q6:- Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).

try:
    a=int(input("enter first number:-"))
    b=int(input("enter second number:-"))

    result=a/b
    print("result",result)

except ZeroDivisionError:
    print("diverstion by zero is not allowd")

else:
    print("calculation successful")

finally:
    print("program end")
