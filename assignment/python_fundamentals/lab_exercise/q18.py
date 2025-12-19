# Q18. Write a Python program that uses a custom iterator to iterate over a list of integers.

class MyIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

nums = [10, 20, 30, 40, 50]

obj = MyIterator(nums)

for i in obj:
    print(i)
