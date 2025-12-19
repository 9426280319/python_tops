# Q32. Write a Python program to apply the map() function to square a list of numbers.

numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * x, numbers)

print(list(result))
