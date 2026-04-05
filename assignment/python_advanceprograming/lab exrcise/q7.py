# Q7: Python program to demonstrate handling multiple exceptions

try:
    x=int(input("enter a number:-"))
    y=int(input("enter b number:-"))

    result=x/y
    print("result:-",result)

except ZeroDivisionError:
    print("can't multiplay by zero")
except ValueError:
    print("only numbers are allows")

else:
    print("done")

finally:
    print("program is end")