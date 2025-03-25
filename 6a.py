o = set()
ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]
with open("6i.txt") as f:
    i = 0
    for l in f:
        if i == 0:
            w = len(l) - 1
        for j in range(len(l)):
            if l[j] == "#":
                o.add((i, j))
            elif l[j] == "^":
                p = (i, j)
        i += 1
    h = i
c = 0
cds = 0
d = set()
while 0 <= p[0] < h and 0 <= p[1] < w:
    if (p[0] + ds[cds][0], p[1] + ds[cds][1]) in o:
        cds = (cds + 1) % 4
    if p not in d:
        c += 1
        d.add(p)
    p = (p[0] + ds[cds][0], p[1] + ds[cds][1])
print(c)
