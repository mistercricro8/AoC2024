def pp(w, o, p, di, dj):
    ep = (p[0] + di, p[1] + dj)
    if ep in w:
        return
    if ep in o:
        q = [ep,]
        fp = (ep[0] + di, ep[1] + dj)
        while fp in o and fp not in w:
            q.append(fp)
            fp = (fp[0] + di, fp[1] + dj)
        if fp not in w:
            for i in range(len(q) - 1, -1, -1):
                o.remove(q[i])
                o.add((q[i][0] + di, q[i][1] + dj))
        else:
            return
    p[0] = ep[0]
    p[1] = ep[1]


with open("15i.txt") as f:
    w = set()
    o = set()
    l = f.readline().strip()
    i = 0
    while l != "":
        for j in range(len(l)):
            if l[j] == '#':
                w.add((i, j,))
            elif l[j] == 'O':
                o.add((i, j,))
            elif l[j] == '@':
                p = [i, j,]
        l = f.readline().strip()
        i += 1
    l = f.readline().strip()
    while l != "":
        for a in l:
            if a == '<':
                pp(w, o, p, 0, -1)
            elif a == '>':
                pp(w, o, p, 0, 1)
            elif a == '^':
                pp(w, o, p, -1, 0)
            elif a == 'v':
                pp(w, o, p, 1, 0)
        l = f.readline().strip()
    s = 0
    for e in o:
        s += 100 * e[0] + e[1]
    print(s)