"""f = open("demo.txt","a")
f.write("Programmers..")
f.close()

f = open("doc.txt","r")
print(f.read())"""

import os
if os.path.exists("demo.txt"):
    print(os.remove("demo.txt"))
else:
    print("file doesn't exits")
