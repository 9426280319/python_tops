# Q12. Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if.

age = int(input("Enter age: "))
weight = int(input("Enter weight: "))

if age >= 18:
    if weight >= 50:
        print("Eligible for blood donation")
    else:
        print("Not eligible: the weight is low")
else:
    print("Not eligible: the age is low")
