def ss(m, ck, i, j, c, w, h, d):
    if i < 0 or i >= h or j < 0 or j >= w or ck[i][j] == 1:
        return 0
    if c == 9:
        if (i, j) not in d:
            d.add((i, j))
            return 1
        return 0
    ck[i][j] = True
    s = 0
    if i + 1 < h and m[i + 1][j] == c + 1:
        s += ss(m, ck, i + 1, j, c + 1, w, h, d)
    if i - 1 >= 0 and m[i - 1][j] == c + 1:
        s += ss(m, ck, i - 1, j, c + 1, w, h, d)
    if j + 1 < h and m[i][j + 1] == c + 1:
        s += ss(m, ck, i, j + 1, c + 1, w, h, d)
    if j - 1 >= 0 and m[i][j - 1] == c + 1:
        s += ss(m, ck, i, j - 1, c + 1, w, h, d)
    ck[i][j] = False
    return s


with open("10i.txt") as f:
    li = f.readline().strip()
    w = len(li)
    i = 0
    m = []
    while li != "":
        m.append([int(x) for x in li])
        i += 1
        li = f.readline().strip()
    h = i
    ck = [[False for x in range(w)] for y in range(h)]
    s = 0
    for i in range(h):
        for j in range(w):
            if m[i][j] == 0:
                d = set()
                s += ss(m, ck, i, j, 0, w, h, d)
    print(s)