def ccds(cds, p, d, si, sj, h, w, pt):
    c = 0
    if cds == 0 and p[0] > 0:
        if p[0] in si:
            ex = -1
            for e in si[p[0]]:
                if e > p[1]:
                    ex = e
                    break
            if ex != -1:
                if (p[0], ex, 1) in d:
                    c += 1
                else:
                    d.add((p[0], ex, 1))
                    pt.append((p[0], ex, 1))
                    c += ccds(1, (p[0], ex - 1), d, si, sj, h, w, pt)
    elif cds == 1 and p[1] < w - 1:
        if p[1] in sj:
            ex = -1
            for e in sj[p[1]]:
                if e > p[0]:
                    ex = e
                    break
            if ex != -1:
                if (ex, p[1], 2) in d:
                    c += 1
                else:
                    d.add((ex, p[1], 2))
                    pt.append((ex, p[1], 2))
                    c += ccds(2, (ex - 1, p[1]), d, si, sj, h, w, pt)
    elif cds == 2 and p[0] < h - 1:
        if p[0] in si:
            ex = -1
            for ee in range(len(si[p[0]]) - 1, -1, -1):
                e = si[p[0]][ee]
                if e < p[1]:
                    ex = e
                    break
            if ex != -1:
                if (p[0], ex, 3) in d:
                    c += 1
                else:
                    d.add((p[0], ex, 3))
                    pt.append((p[0], ex, 3))
                    c += ccds(3, (p[0], ex + 1), d, si, sj, h, w, pt)
    elif cds == 3 and p[1] > 0:
        if p[1] in sj:
            ex = -1
            for ee in range(len(sj[p[1]]) - 1, -1, -1):
                e = sj[p[1]][ee]
                if e < p[0]:
                    ex = e
                    break
            if ex != -1:
                if (ex, p[1], 0) in d:
                    c += 1
                else:
                    d.add((ex, p[1], 0))
                    pt.append((ex, p[1], 0))
                    c += ccds(0, (ex + 1, p[1]), d, si, sj, h, w, pt)
    return c


def aps(l, e):
    d = False
    for i in range(len(l)):
        if e < l[i]:
            l.insert(i, e)
            d = True
            break
    if not d:
        l.append(e)


def chk(d, n, p, si, sj, cds, h, w, ph):
    if (n[0], n[1]) in ph:
        return 0
    d2 = d.copy()
    c = 0
    d2.add(n)
    if n[0] not in si:
        si[n[0]] = []
    if n[1] not in sj:
        sj[n[1]] = []
    aps(si[n[0]], n[1])
    aps(sj[n[1]], n[0])
    pt = []
    rr = ccds(cds, p, d2, si, sj, h, w, pt)
    if rr == 1:
        if (n[0], n[1]) not in sl:
            c += 1
            sl.add((n[0], n[1]))
    si[n[0]].remove(n[1])
    sj[n[1]].remove(n[0])
    return c


si = {}
sj = {}
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
                if i not in si:
                    si[i] = []
                si[i].append(j)
                if j not in sj:
                    sj[j] = []
                sj[j].append(i)
            elif l[j] == "^":
                p = [
                    i,
                    j,
                ]
        i += 1
    h = i
cds = 0
d = set()
c = 0
sl = set()
ph = set()
nns = {}
while 0 <= p[0] < h and 0 <= p[1] < w:
    n = (p[0] + ds[cds][0], p[1] + ds[cds][1], cds)
    vvv = True
    ph.add((p[0], p[1]))
    while (n[0], n[1]) in o:
        d.add(n)
        cds = (cds + 1) % 4
        nns[(n[0], n[1])] = cds
        n = (p[0] + ds[cds][0], p[1] + ds[cds][1], cds)
        c += chk(d, n, p, si, sj, cds, h, w, ph)
        vvv = False
    if vvv:
        c += chk(d, n, p, si, sj, cds, h, w, ph)
    p[0] += ds[cds][0]
    p[1] += ds[cds][1]
print(c)