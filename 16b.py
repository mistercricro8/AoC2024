import heapq

dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def gb(si, sj, i, j, r, c, p, s):
    if i == si and j == sj:
        return
    pc = p[i][j][r]
    for w in range(4):
        if c[pc[0]][pc[1]][w] != None and c[pc[0]][pc[1]][w] + (1 if w == r else 1001) == c[i][j][r]:
            t = (pc[0], pc[1], )
            if not t in s:
                s.add(t)
            gb(si, sj, t[0], t[1], w, c, p, s)

def ss(ws, i, j, ei, ej, v, c, p):
    ni = i
    nj = j
    d = 0
    for x in range(4):
        c[i][j][x] = 0 
    q = [(0, i, j, d,),]
    while len(q) > 0:
        _, i, j, d = heapq.heappop(q)
        v[i][j][d] = True
        for w in range(-1, 2):
            fr = (d + w) % 4
            cdd = dd[fr]
            cdi = i + cdd[0]
            cdj = j + cdd[1]
            if (cdi, cdj,) not in ws and not v[cdi][cdj][fr]:
                df = (1 if w == 0 else 1001)
                if c[cdi][cdj][fr] > c[i][j][d] + df:
                    c[cdi][cdj][fr] = c[i][j][d] + df
                    p[cdi][cdj][fr] = (i, j, d,)
                    heapq.heappush(q, (c[cdi][cdj][fr], cdi, cdj, fr,))
    m = 0
    for x in range(4):
        if c[ei][ej][x] < c[ei][ej][m]:
            m = x
    s = set()
    s.add((ei, ej,))
    gb(ni, nj, ei, ej, m, c, p, s)
    return len(s)


with open("16i.txt") as f:
    l = f.readline().strip()
    i = 0
    ws = set()
    w = len(l)
    while l != "":
        for j in range(len(l)):
            if l[j] == "#":
                ws.add((i, j,))
            elif l[j] == "S":
                s = [i,j,]
            elif l[j] == "E":
                e = [i,j,]
        i += 1
        l = f.readline().strip()
    me = {}
    v = [[[False for _ in range(4)] for _ in range(w)] for _ in range(i)]
    c = [[[float("inf") for _ in range(4)] for _ in range(w)] for _ in range(i)]
    p = [[[None for _ in range(4)] for _ in range(w)] for _ in range(i)]
    print(ss(ws, s[0], s[1], e[0], e[1], v, c, p))

