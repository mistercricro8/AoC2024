AND = "AND"
OR = "OR"
XOR = "XOR"

with open("24i.txt") as f:
    li = f.readline().strip()
    vs = {}
    while li != "":
        k, v = li.split(": ")
        vs[k] = v == "1"
        li = f.readline().strip()
    li = f.readline().strip()
    co = []
    while li != "":
        ar = li.split()
        co.append([ar[0], ar[1], ar[2], ar[4], False,])
        li = f.readline().strip()
    while True:
        d = False
        for i in range(len(co)):
            ar = co[i]
            if ar[4] or ar[0] not in vs or ar[2] not in vs:
                continue
            d = True
            if ar[1] == AND:
                r = vs[ar[0]] and vs[ar[2]]
            elif ar[1] == OR:
                r = vs[ar[0]] or vs[ar[2]]
            elif ar[1] == XOR:
                r = vs[ar[0]] ^ vs[ar[2]]
            if ar[3] not in vs:
                vs[ar[3]] = r
                ar[4] = True
        if not d:
            break
    v = 0
    c = 1
    i = 0
    ky = "z{va:02d}".format(va=i)
    while ky in vs:
        v += vs[ky] * c
        c *= 2
        i += 1
        ky = "z{va:02d}".format(va=i)
    print(v)