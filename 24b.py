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
    hi = "z00"
    while li != "":
        ar = li.split()
        co.append([ar[0], ar[1], ar[2], ar[4],])
        if ar[4][0] == 'z' and int(ar[4][1:]) > int(hi[1:]):
            hi = ar[4]
        li = f.readline().strip()
    m = set()
    for p1, op, p2, re in co:
        if re[0] == 'z' and re != hi and op != XOR:
            m.add(re)
        elif op == XOR and re[0] != 'z' and p1[0] != 'x' and p1[0] != 'y' and p2[0] != 'x' and p2[0] != 'y':
            m.add(re)
        elif op == AND and p1 != "x00" and p2 != "x00":
            for sp1, sop, sp2, sre in co:
                if sop != OR and (sp1 == re or sp2 == re):
                    m.add(re)
        elif op == XOR or op == OR:
            for sp1, sop, sp2, sre in co:
                if sop == OR and (sp1 == re or sp2 == re):
                    m.add(re)
    ms = list(m)
    ms.sort()
    print(",".join(ms))