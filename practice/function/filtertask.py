subjects = ["Python","android","php","java","sql","cpp","op","p"]

k = filter(lambda x : ('p' in x.lower()) , subjects)
print(list(k))
