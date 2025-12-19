# Q17.  Write a generator function that generates the first 10 even numbers.

def even_numbers():
    num = 2
    for i in range(10):
        yield num
        num += 2

for even in even_numbers():
    print(even)

