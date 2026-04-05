# Q4:- • Write a Python program to read the contents of a file and print them on the console.

f=open("myfile.txt")
data=f.readline()
print(data)
f.close()