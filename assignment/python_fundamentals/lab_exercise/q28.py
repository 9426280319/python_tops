# Q28. Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue
# statement. List1 = ['apple', 'banana', 'mango']

list1 = ['apple', 'banana', 'mango']

for item in list1:
    if item == 'banana':
        continue
    print(item)
