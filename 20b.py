import heapq

dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def ss(ws, i, j, ei, ej, c, p):
    c[i][j] = 0
    q = [(0, i, j),]
    while len(q) > 0:
        d, i, j = heapq.heappop(q)
        for di, dj in dd:
            ni, nj = i + di, j + dj
            if ws[ni][nj]:
                continue
            if c[ni][nj] > d + 1:
                c[ni][nj] = d + 1
                p[ni][nj] = (i, j)
                heapq.heappush(q, (d + 1, ni, nj))
    return c[ei][ej]


def bp(si, sj, pt, ws, w, h):
    r = 20
    vt = max(si - r, 0)
    vb = min(si + r + 1, h)
    hl = max(sj - r, 0)
    hr = min(sj + r + 1, w)
    c = 0
    for u in range(vt, vb):
        for v in range(hl, hr):
            ds = abs(si - u) + abs(sj - v)
            if ws[u][v] or ds > r:
                continue
            if pt[(u, v)] - pt[(si, sj)] - ds >= 100:
                c += 1
    return c

            


with open("20i.txt") as f:
    l = f.readline().strip()
    ws = []
    i = 0
    w = len(l)
    while l != "":
        ws.append([False for _ in range(w)])
        for j in range(w):
            if l[j] == "#":
                ws[i][j] = True
            elif l[j] == "S":
                si, sj = i, j
            elif l[j] == "E":
                ei, ej = i, j
        i += 1
        l = f.readline().strip()
    h = i
    c = [[float("inf") for _ in range(w)] for _ in range(h)]
    p = [[None for _ in range(w)] for _ in range(h)]
    bt = ss(ws, si, sj, ei, ej, c, p)
    pt = {}
    v = 0
    i, j = ei, ej
    while (i, j) != (si, sj):
        pt[(i, j)] = v
        i, j = p[i][j]
        v += 1
    pt[(si, sj)] = v
    tt = 0
    for ky in pt.keys():
        pi, pj = ky[0], ky[1]
        tt += bp(pi, pj, pt, ws, w, h)
    print(tt)
# 971737

