def ss(t, m, co, v, l, i, j):
    if i < 0 or i >= l or j < 0 or j >= l:
        return 0
    v[i][j] = True
    c = 1
    if i + 1 < l and m[i + 1][j] == t:
        if not v[i + 1][j]:
            c += ss(t, m, co, v, l, i + 1, j)
    else:
        co.add((i, j, i + 1, j))
    if i - 1 >= 0 and m[i - 1][j] == t:
        if not v[i - 1][j]:
            c += ss(t, m, co, v, l, i - 1, j)
    else:
        co.add((i, j, i - 1, j))
    if j + 1 < l and m[i][j + 1] == t:
        if not v[i][j + 1]:
            c += ss(t, m, co, v, l, i, j + 1)
    else:
        co.add((i, j, i, j + 1))
    if j - 1 >= 0 and m[i][j - 1] == t:
        if not v[i][j - 1]:
            c += ss(t, m, co, v, l, i, j - 1)
    else:
        co.add((i, j, i, j - 1))
    return c


with open("12i.txt") as f:
    m = [li.strip() for li in f]
    l = len(m)

v = [[False for _ in range(l)] for _ in range(l)]
cc = 0
for i in range(l):
    for j in range(l):
        if v[i][j]:
            continue
        co = set()
        lu = ss(m[i][j], m, co, v, l, i, j)
        dh = {}
        dv = {}
        lc = 0
        while len(co) > 0:
            c = co.pop()
            lc += 1
            if c[0] == c[2]:
                k = (c[0] - 1, c[1], c[2] - 1, c[3])
                while k in co:
                    co.remove(k)
                    k = (k[0] - 1, k[1], k[2] - 1, k[3])
                k = (c[0] + 1, c[1], c[2] + 1, c[3])
                while k in co:
                    co.remove(k)
                    k = (k[0] + 1, k[1], k[2] + 1, k[3])
            elif c[1] == c[3]:
                k = (c[0], c[1] - 1, c[2], c[3] - 1)
                while k in co:
                    co.remove(k)
                    k = (k[0], k[1] - 1, k[2], k[3] - 1)
                k = (c[0], c[1] + 1, c[2], c[3] + 1)
                while k in co:
                    co.remove(k)
                    k = (k[0], k[1] + 1, k[2], k[3] + 1)
        cc += lu * lc

print(cc)