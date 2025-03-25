with open("25i.txt") as f:
    li = f.readline().strip()
    ls = []
    ks = []
    lth = len(li)
    while True:
        if li[0] == '#':
            h = -1
            ls.append([-1 for i in range(lth)])
            el = ls[-1]
            while li != "":
                for i in range(lth):
                    if el[i] == -1 and li[i] == '.':
                        el[i] = h
                h += 1
                li = f.readline().strip()
        else:
            h = -1
            ks.append([-1 for i in range(lth)])
            el = ks[-1]
            while li != "":
                for i in range(lth):
                    if el[i] == -1 and li[i] == '#':
                        el[i] = lth - h
                h += 1
                li = f.readline().strip()
        li = f.readline().strip()
        if li == "":
            break
    c = 0
    for l in ls:
        for k in ks:
            v = True
            for i in range(lth):
                if l[i] + k[i] > lth:
                    v = False
                    break
            if v:
                c += 1
    print(c)           