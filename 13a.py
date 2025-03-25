def ss(t, m, co, v, l, i, j):
    if i < 0 or i >= l or j < 0 or j >= l:
        return
    v[i][j] = True
    if i + 1 < l and m[i + 1][j] == t:
        if (i, j, i + 1, j) not in co and (i + 1, j, i, j) not in co:
            co.add((i, j, i + 1, j))
            if not v[i + 1][j]:
                ss(t, m, co, v, l, i + 1, j)
    if i - 1 >= 0 and m[i - 1][j] == t:
        if (i, j, i - 1, j) not in co and (i - 1, j, i, j) not in co:
            co.add((i, j, i - 1, j))
            if not v[i - 1][j]:
                ss(t, m, co, v, l, i - 1, j)
    if j + 1 < l and m[i][j + 1] == t:
        if (i, j, i, j + 1) not in co and (i, j + 1, i, j) not in co:
            co.add((i, j, i, j + 1))
            if not v[i][j + 1]:
                ss(t, m, co, v, l, i, j + 1)
    if j - 1 >= 0 and m[i][j - 1] == t:
        if (i, j, i, j - 1) not in co and (i, j - 1, i, j) not in co:
            co.add((i, j, i, j - 1))
            if not v[i][j - 1]:
                ss(t, m, co, v, l, i, j - 1)


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
        ss(m[i][j], m, co, v, l, i, j)
        lc = len(co)
        u = set()
        for c in co:
            if (c[0], c[1]) not in u:
                u.add((c[0], c[1]))
            if (c[2], c[3]) not in u:
                u.add((c[2], c[3]))
        lu = len(u)
        lu = 1 if lu == 0 else lu
        cc += lu * (lu * 4 - lc * 2)

print(cc)
