# Q34. Write a Python program that filters out even numbers using the filter() function.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
