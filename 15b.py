def pp(w, o, p, di, dj):
    ep = (p[0] + di, p[1] + dj)
    ep2 = (p[0] + di, p[1] + dj - 1)
    if ep in w or ep2 in w:
        return
    eo1 = ep in o
    eo2 = ep2 in o
    if eo1 or eo2:
        q = []
        if eo1:
            fp = ep
            fp2 = ep2
        else:
            fp = ep2
            fp2 = ep
        dj2 = dj * 2
        dt = True
        if di == 0:
            q.append(fp)
            fp = (fp[0], fp[1] + dj2)
            fp2 = (fp2[0], fp2[1] + dj2)
            while fp in o and fp not in w and fp2 not in w:
                q.append(fp)
                fp = (fp[0], fp[1] + dj2)
                fp2 = (fp2[0], fp2[1] + dj2)
            dt = fp not in w and fp2 not in w
        else:
            b = [fp,]
            while len(b) > 0:
                v = True
                for e in b:
                    if (e[0] + di, e[1] - 1) in w or (e[0] + di, e[1]) in w or (e[0] + di, e[1] + 1) in w:
                        v = False
                        break
                if not v:
                    dt = False
                    break
                c = []
                for e in b:
                    q.append(e)
                    for i in range(-1, 2):
                        fps = (e[0] + di, e[1] + i)
                        if fps in o and fps not in c:
                            c.append(fps)
                b = c            
        if dt:
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
    wi = len(l) * 2
    i = 0
    while l != "":
        for j in range(len(l)):
            if l[j] == '#':
                w.add((i, j * 2,))
            elif l[j] == 'O':
                o.add((i, j * 2,))
            elif l[j] == '@':
                p = [i, j * 2,]
        l = f.readline().strip()
        i += 1
    h = i
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
            '''
            ma = [["." for _ in range(wi)] for _ in range(h)]
            for e in w:
                ma[e[0]][e[1]] = "#"
                ma[e[0]][e[1] + 1] = "#"
            for e in o:
                ma[e[0]][e[1]] = "["
                ma[e[0]][e[1] + 1] = "]"
            ma[p[0]][p[1]] = "@"
            print()
            print(a)
            for e in ma:
                print("".join(e))
            '''
        l = f.readline().strip()
    s = 0


    for e in o:
        s += 100 * e[0] + e[1]
    print(s)