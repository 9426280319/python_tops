import re
text="my name is sneha. i am a backend devloper"
data=re.match("sneha",text)

if data:
    print("data match ")
else:
    print("data not match")