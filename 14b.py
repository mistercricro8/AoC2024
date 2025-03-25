w = 101
h = 103
with open("14i.txt") as f:
    li = f.readline().split()
    co = [[0 for _ in range(2)] for _ in range(2)]
    ps = []
    vs = []
    while len(li) > 0:
        p = li[0][2:].split(",")
        p = (int(p[0]), int(p[1]))
        v = li[1][2:].split(",")
        v = (int(v[0]), int(v[1]))
        ps.append(p)
        vs.append(v)
        li = f.readline().split()

for i in range(20000):
    for j in range(len(ps)):
        ps[j] = ((ps[j][0] + vs[j][0]) % w, (ps[j][1] + vs[j][1]) % h)
    co = [[0 for _ in range(2)] for _ in range(2)]
    for p in ps:
        fpx = p[0]
        fpy = p[1]
        if fpx != w // 2 and fpy != h // 2:
            co[fpy // ((h + 1) // 2)][fpx // ((w + 1) // 2)] += 1
    s = 1
    for r in co:
        for e in r:
            s *= e
    if s < 100000000:
        print(f"=============={i+1}==============")
        m = [[" " for _ in range(w)] for _ in range(h)]
        for p in ps:
            m[p[1]][p[0]] = "#"
        for r in m:
            print("".join(r))