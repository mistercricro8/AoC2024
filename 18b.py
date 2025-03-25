import heapq

def ss(ws, i, j, ei, ej, c, w, p, h):
    c[i][j] = 0
    q = [(0, i, j),]
    while len(q) > 0:
        d, i, j = heapq.heappop(q)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= h or nj < 0 or nj >= w or (ni, nj) in ws:
                continue
            if c[ni][nj] > d + 1:
                c[ni][nj] = d + 1
                p[ni][nj] = (i, j)
                heapq.heappush(q, (d + 1, ni, nj))
    return c[ei][ej]

with open("18i.txt") as f:
    l = f.readline().strip()
    ws = set()
    w = h = 71
    x, y = l.split(",")
    ws.add((int(y), int(x),))
    l = f.readline().strip()
    c = [[float("inf") for _ in range(w)] for _ in range(h)]
    p = [[None for _ in range(w)] for _ in range(h)]
    ss(ws, 0, 0, w-1, h-1, c, w, p, h)
    pt = set()
    i, j = w-1, h-1
    while p[i][j] is not None:
        pt.add((i, j,))
        i, j = p[i][j]
    while l != "":
        x, y = l.split(",")
        nw = (int(y), int(x),)
        ws.add(nw)
        if nw in pt:
            c = [[float("inf") for _ in range(w)] for _ in range(h)]
            p = [[None for _ in range(w)] for _ in range(h)]
            ss(ws, 0, 0, w-1, h-1, c, w, p, h)
            pt = set()
            i, j = w-1, h-1
            while p[i][j] is not None:
                pt.add((i, j,))
                i, j = p[i][j]
        if c[w-1][h-1] >= float("inf"):
            print(f"{nw[1]},{nw[0]}")
            break
        l = f.readline().strip()