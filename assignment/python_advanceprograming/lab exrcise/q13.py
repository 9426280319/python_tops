import re
text="my name is dev. i am a backend devloper"
data=re.match("dev",text)

if data:
    print("data match ")
else:
    print("data not match")