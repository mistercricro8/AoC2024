with open("2i.txt") as f:
    li = f.readline()
    s = 0
    while li != "":
        r = [int(x) for x in li.split()]
        uv = dv = True
        for i in range(1, len(r)):
            du = r[i] - r[i-1]
            dd = r[i-1] - r[i]
            if uv and not (1 <= du and du <= 3):
                uv = False
            if dv and not (1 <= dd and dd <= 3):
                dv = False
            if not uv and not dv:
                break
        if uv or dv:
            s += 1
        li = f.readline()
    print(s)