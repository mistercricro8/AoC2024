def ss(o, i, pts):
    if i >= len(o):
        return True

    for t in range(len(pts) - 1, -1, -1):
        v = True
        for u in range(len(pts[t])):
            if o[i : i + u + 1] != pts[t][: u + 1]:
                v = False
                break
        if v:
            if ss(o, i + len(pts[t]), pts):
                return True
    return False

with open("19i.txt") as f:
    pts = [x for x in f.readline().strip().split(", ")]
    f.readline()
    li = f.readline().strip()
    s = 0
    while li != "":
        l = len(pts) - 1
        s += ss(li, 0, pts)
        li = f.readline().strip()
    print(s)