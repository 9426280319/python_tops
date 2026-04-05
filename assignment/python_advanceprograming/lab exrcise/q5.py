# Q5:- • Write a Python program to write multiple strings into a file.

strings = [
    "Python is a powerful language.\n",
    "It is easy to learn.\n",
    "File handling is simple in Python.\n"
]

f = open("data.txt", "w")
data=f.writelines(strings)
f.close()

