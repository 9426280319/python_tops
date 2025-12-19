# Q15. Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition.

list1 = ['apple', 'banana', 'mango']
search_item = "strwberry"

found = False

for item in list1:
    if item == search_item:
        found = True
        break

if found:
    print("this Item is exist in list ")
else:
    print("this Item iz not exist in list")
