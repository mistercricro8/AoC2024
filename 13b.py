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
        print(m[i][j])
        co = set()
        lu = ss(m[i][j], m, co, v, l, i, j)
        lc = len(co)
        dh = {}
        dv = {}
        for c in co:
            if c[1] == c[3]:                
                k1 = (c[0], c[2])
                if k1 not in dh:
                    dh[k1] = set()
                    dh[k1].add(c[1])
                    print(f"h side init ({k1}), from ({c[0]}, {c[1]}) to ({c[2]}, {c[3]})")
                else:
                    e = dh[k1]
                    if (k1[0], c[1]-1, k1[1], c[1]-1) in co or (k1[0], c[1]+1, k1[1], c[1]+1) in co:
                        lc -= 1
                        print(f"h wall ({k1}), from ({c[0]}, {c[1]}) to ({c[2]}, {c[3]}) is already a side")
                    else:
                        e.add(c[1])
                        print(f"dup code ({k1}), new h side, from ({c[0]}, {c[1]}) to ({c[2]}, {c[3]})")
            elif c[0] == c[2]:
                k2 = (c[1], c[3])
                if k2 not in dv:
                    dv[k2] = set()
                    dv[k2].add(c[0])
                    print(f"v side init ({k2}), from ({c[0]}, {c[1]}) to ({c[2]}, {c[3]})")
                else:
                    e = dv[k2]
                    if (c[0]-1, k2[0], c[0]-1, k2[1]) in co or (c[0]+1, k2[0], c[0]+1, k2[1]) in co:
                        lc -= 1
                        print(f"v wall ({k2}), from ({c[0]}, {c[1]}) to ({c[2]}, {c[3]}) is already a side")
                    else:
                        e.add(c[0])
                        print(f"dup code ({k2}), new v side, from ({c[0]}, {c[1]}) to ({c[2]}, {c[3]})")
        cc += lu * lc

print(cc)
