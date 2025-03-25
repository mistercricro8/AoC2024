def ss(me, o, i, pts):
    if i >= len(o):
        return 1
    if me[i] != -1:
        return me[i]
    s = 0
    for t in range(len(pts) - 1, -1, -1):
        v = True
        for u in range(len(pts[t])):
            if o[i : i + u + 1] != pts[t][: u + 1]:
                v = False
                break
        if v:
            s += ss(me, o, i + len(pts[t]), pts)
    me[i] = s
    return s

with open("19i.txt") as f:
    pts = [x for x in f.readline().strip().split(", ")]
    f.readline()
    li = f.readline().strip()
    s = 0
    while li != "":
        me = [-1] * len(li)
        l = len(pts) - 1
        s += ss(me, li, 0, pts)
        li = f.readline().strip()
    print(s)