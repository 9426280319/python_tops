from functools import reduce

l = [1,2,3,4,5,6,7,8]

even_numbers = list(filter(lambda x: x % 2 == 0, l))

result = reduce(lambda x,y : x*y , even_numbers)

print(result)
