# Q10. Practical Example 6: Write a Python program to check if a number is prime using if_else.

num = int(input("Enter a number: "))

if num > 1:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not prime number")
else:
    print("Not prime number")
