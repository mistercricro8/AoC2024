import heapq

def ss(ws, i, j, ei, ej, c, w, h):
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
                heapq.heappush(q, (d + 1, ni, nj))
    return c[ei][ej]

with open("18i.txt") as f:
    l = f.readline().strip()
    ws = set()
    w = h = 71
    b = 1024
    while l != "" and b > 0:
        x, y = l.split(",")
        ws.add((int(y), int(x),))
        l = f.readline().strip()
        b -= 1
    c = [[float("inf") for _ in range(w)] for _ in range(h)]
    print(ss(ws, 0, 0, w-1, h-1, c, w, h))
