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
    co = 0
    for ky in pt.keys():
        for di, dj in dd:
            ni, nj = ky[0] + di, ky[1] + dj
            ni2, nj2 = ky[0] + di * 2, ky[1] + dj * 2
            if ws[ni][nj] and ni2 >= 0 and ni2 < h and nj2 >= 0 and nj2 < w and not ws[ni2][nj2]:
                df = pt[(ni2, nj2)] - pt[ky] - 2
                if df >= 100:
                    co += 1
    print(co)

