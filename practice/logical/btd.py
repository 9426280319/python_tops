number = 10011010010
dev=0
sum = 0
while number!=0:
    rem = number%10
    sum+=rem*pow(2,dev)
    number//=10
    dev+=1

print(sum)