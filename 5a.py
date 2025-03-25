with open("5i.txt") as f:
    l = f.readline().strip()
    d = []
    while l != "":
        a, b = l.split("|")
        d.append((a, b))
        l = f.readline().strip()
    l = f.readline().strip()
    s = 0
    d = set(d)
    while l != "":
        c = l.split(",")
        v = True
        for i in range(len(c)):
            for j in range(i, len(c)):
                if (c[j], c[i]) in d:
                    v = False
                    break
        if v:
            s += int(c[len(c) // 2])
        l = f.readline().strip()
    print(s)
