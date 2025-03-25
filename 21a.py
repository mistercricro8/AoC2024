dd = [(3, 1), (2, 0), (2, 1), (2, 2), (1, 0), (1, 1), (1, 2), (0, 0), (0, 1), (0, 2)]
dr = [(1, 1), (0, 1), (1, 2), (1, 0), (0, 2)]


def cb(i, j, ei, ej, ca, hi, hj):
    if i == ei and j == ej:
        ca.append([4])
        return
    si, sj = i, j
    if i != ei:
        pt = []
        v = True
        while i != ei:
            if i == hi and j == hj:
                v = False
                break
            if i < ei:
                i += 1
                pt.append(0)
            else:
                i -= 1
                pt.append(1)
        while j != ej:
            if i == hi and j == hj:
                v = False
                break
            if j < ej:
                j += 1
                pt.append(2)
            else:
                j -= 1
                pt.append(3)
        pt.append(4)
        if v:
            ca.append(pt)
    i, j = si, sj
    if j != ej:
        pt = []
        v = True
        while j != ej:
            if j == hi and i == hj:
                v = False
                break
            if j < ej:
                j += 1
                pt.append(2)
            else:
                j -= 1
                pt.append(3)
        while i != ei:
            if i == hi and j == hj:
                v = False
                break
            if i < ei:
                i += 1
                pt.append(0)
            else:
                i -= 1
                pt.append(1)
        pt.append(4)
        if v:
            ca.append(pt)


def pm(ca, nca):
    fca = []
    if len(ca) == 0:
        for nc in nca:
            fca.append(nc)
    else:
        for c in ca:
            for nc in nca:
                fca.append(c + nc)
    return fca

def it(me, ca, dp):
    if dp == 0:
        nn = float("inf")
        for c in ca:
            cx = len(c)
            if cx < nn:
                nn = cx
        return nn
    si, sj = 0, 2
    mn = float("inf")
    for c in ca:
        s = 0
        for p in c:
            d = dr[p]
            ei, ej = d[0], d[1]
            ky = (si, sj, ei, ej, dp)
            if ky not in me:
                nca = []
                cb(si, sj, ei, ej, nca, 0, 0)
                cx = it(me, nca, dp - 1)
                me[ky] = cx
            s += me[ky]
            si, sj = ei, ej
        if s < mn:
            mn = s
    return mn

with open("21i.txt") as f:
    li = f.readline().strip()[:-1]
    w = 3
    h = 4
    s = 0
    me = {}
    while li != "":
        si, sj = 3, 2
        cc = 0
        for c in li:
            d = dd[int(c)]
            ei, ej = d[0], d[1]
            nca = []
            cb(si, sj, ei, ej, nca, 3, 0)
            cc += it(me, nca, 2)
            si, sj = ei, ej
        ei, ej = 3, 2
        nca = []
        cb(si, sj, ei, ej, nca, 3, 0)
        cc += it(me, nca, 2)
        cx = int(li) * cc
        s += cx
        li = f.readline().strip()[:-1]
    print(s)
