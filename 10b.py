def ss(me, m, ck, i, j, c, w, h):
    if i < 0 or i >= h or j < 0 or j >= w or ck[i][j] == 1:
        return 0
    if c == 9:
        me[i][j] = 1
    if me[i][j] == -1:
        ck[i][j] = True
        me[i][j] = 0
        if i + 1 < h and m[i + 1][j] == c + 1:
            me[i][j] += ss(me, m, ck, i + 1, j, c + 1, w, h)
        if i - 1 >= 0 and m[i - 1][j] == c + 1:
            me[i][j] += ss(me, m, ck, i - 1, j, c + 1, w, h)
        if j + 1 < h and m[i][j + 1] == c + 1:
            me[i][j] += ss(me, m, ck, i, j + 1, c + 1, w, h)
        if j - 1 >= 0 and m[i][j - 1] == c + 1:
            me[i][j] += ss(me, m, ck, i, j - 1, c + 1, w, h)
        ck[i][j] = False
    return me[i][j]


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
    me = [[-1 for x in range(w)] for y in range(h)]
    ck = [[False for x in range(w)] for y in range(h)]
    s = 0
    for i in range(h):
        for j in range(w):
            if m[i][j] == 0:
                s += ss(me, m, ck, i, j, 0, w, h)
                me = [[-1 for x in range(w)] for y in range(h)]
    print(s)