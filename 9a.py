with open("9i.txt") as f:
    l = f.readline().strip()
a = []
o = True
i = 0
for c in l:
    if o:
        for _ in range(int(c)):
            a.append(i)
        i += 1
    else:
        for _ in range(int(c)):
            a.append(-1)
    o = not o
j = len(a) - 1
for i in range(len(a)):
    if i >= j:
        break
    if a[i] == -1:
        while a[j] == -1:
            j -= 1
        (a[i], a[j]) = (a[j], a[i])
s = 0
i = 0
while a[i] != -1:
    s += i * a[i]
    i += 1
print(s)