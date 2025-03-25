import re
with open("3i.txt") as f:
    i = f.read()
ms = re.findall(r"(do|don't|mul)\((\d+,\d+|)\)", i)
s = 0
e = True
for m in ms:
    if m[0] == "do" and m[1] == "":
        e = True
    elif m[0] == "don't" and m[1] == "":
        e = False
    elif m[0] == "mul" and e:
        a, b = [int(x) for x in m[1].split(",")]
        s += a * b
print(s)