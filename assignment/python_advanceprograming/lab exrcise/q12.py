import re
text="my name is sneha"
data=re.search("sneha",text)

if data:
    print("word found at position:",data.start())
else:
    print("word not found")