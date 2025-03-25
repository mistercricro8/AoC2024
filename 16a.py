import heapq

dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def ss(ws, i, j, ei, ej, v, c):
    d = 0
    c[i][j] = 0
    q = [(0, i, j, d,),]
    while len(q) > 0:
        p, i, j, d = heapq.heappop(q)
        v[i][j] = True
        for w in range(-1, 2):
            fr = (d + w) % 4
            cdd = dd[fr]
            cdi = i + cdd[0]
            cdj = j + cdd[1]
            if (cdi, cdj,) not in ws and not v[cdi][cdj]:
                df = (1 if w == 0 else 1001)
                if c[cdi][cdj] > c[i][j] + df:
                    c[cdi][cdj] = c[i][j] + df
                    heapq.heappush(q, (c[cdi][cdj], cdi, cdj, fr,))
    return c[ei][ej]


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
    v = [[False for _ in range(w)] for _ in range(i)]
    c = [[float("inf") for _ in range(w)] for _ in range(i)]
    print(ss(ws, s[0], s[1], e[0], e[1], v, c))
