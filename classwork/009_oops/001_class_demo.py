class pen:
    price = 10
    color = "red"

    #function member 
    def to_write(self):

        print("writing something...")
        print(self.price,self.color)

    def display(self):
        print(self.price,self.color)

p2 = pen()
print(p2.price)
print(p2.color)
p2.to_write()

p2.price=98
p2.color="purple"
p2.to_write()
