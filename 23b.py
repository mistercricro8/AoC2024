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
l = []
for ky in d.keys():
    if ky[0] == "t":
        ll = list(d[ky])
        ll.append(ky)
        l.append(ll)
for i in range(len(l) - 1, -1, -1):
    la = l[i]
    j = 0
    while j < len(la):
        k = j + 1
        while k < len(la):
            if la[k] not in d[la[j]]:
                ck = 0
                for u in range(len(la)):
                    if la[k] in d[la[u]]:
                        ck += 1
                cj = 0
                for u in range(len(la)):
                    if la[j] in d[la[u]]:
                        cj += 1
                if ck < cj:
                    la.pop(k)
                else:
                    la.pop(j)
                k -= 1
            k += 1
        j += 1
l.sort(key=lambda x: len(x))
fi = l[-1]
fi.sort()
print(",".join(fi))
