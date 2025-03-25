import re
with open("3i.txt") as f:
    i = f.read()
ms = re.findall(r"mul\((\d+,\d+)\)", i)
s = 0
for m in ms:
    a, b = [int(x) for x in m.split(",")]
    s += a * b
print(s)