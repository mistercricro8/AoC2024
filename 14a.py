w = 101
h = 103
with open("14i.txt") as f:
    li = f.readline().split()
    co = [[0 for _ in range(2)] for _ in range(2)]
    while len(li) > 0:
        p = li[0][2:].split(",")
        p = (int(p[0]), int(p[1]))
        v = li[1][2:].split(",")
        v = (int(v[0]), int(v[1]))
        fpx = (p[0] + v[0] * 100) % w
        fpy = (p[1] + v[1] * 100) % h
        if fpx != w // 2 and fpy != h // 2:
            co[fpy // ((h + 1) // 2)][fpx // ((w + 1) // 2)] += 1
        li = f.readline().split()
    s = 1
    for r in co:
        for e in r:
            s *= e
    print(s)