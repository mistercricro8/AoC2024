with open("23i.txt") as f:
    li = f.readline().strip()
    d = {}
    while li != "":
        a, b = li.split("-")
        if a not in d:
            d[a] = set()
        d[a].add(b)
        if b not in d:
            d[b] = set()
        d[b].add(a)
        li = f.readline().strip()
s = 0
u = set()
for ky in d.keys():
    if ky[0] == "t":
        l = list(d[ky])
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if i != j and l[i] not in u and l[j] not in u:
                    if l[j] in d[l[i]]:
                        s += 1
        u.add(ky)
print(s)
        