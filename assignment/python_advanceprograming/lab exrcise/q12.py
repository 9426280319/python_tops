import re
text="my name is dev"
data=re.search("dev",text)

if data:
    print("word found at position:",data.start())
else:
    print("word not found")