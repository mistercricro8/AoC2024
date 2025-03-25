def kmp(c, i, j, di, dj, n, pat):
    if n < len(pat):
        return 0
    m = 4
    co = 0
    t = [i, j]
    p = 0
    cc = 0
    while cc < n:
        if c[t[0]][t[1]] == pat[p]:
            p += 1
            t[0] += di
            t[1] += dj
            cc += 1
            if p == m:
                co += 1
                p = 0
        else:
            if p != 0:
                p = 0
            else:
                t[0] += di
                t[1] += dj
                cc += 1
    return co


def dd(i1, j1, i2, j2):
    return max(abs(i1 - i2), abs(j1 - j2)) + 1


with open("4i.txt") as f:
    c = f.readlines()
    co = 0
    l = len(c)
    s = l - 1
    for i in range(l):
        c[i] = c[i].strip()
        co += kmp(c, i, 0, 0, 1, l, "XMAS")
        co += kmp(c, i, 0, 0, 1, l, "SAMX")
        d = dd(i, 0, s, s - i)
        co += kmp(c, i, 0, 1, 1, d, "XMAS")
        co += kmp(c, i, 0, 1, 1, d, "SAMX")
        d = dd(i, 0, 0, i)
        co += kmp(c, i, 0, -1, 1, d, "XMAS")
        co += kmp(c, i, 0, -1, 1, d, "SAMX")
        co += kmp(c, 0, i, 1, 0, l, "XMAS")
        co += kmp(c, 0, i, 1, 0, l, "SAMX")
        if i == 0:
            continue
        d = dd(s, i, i, s)
        co += kmp(c, 0, i, 1, 1, d, "XMAS")
        co += kmp(c, 0, i, 1, 1, d, "SAMX")
        d = dd(0, i, s - i, s)
        co += kmp(c, s, i, -1, 1, d, "XMAS")
        co += kmp(c, s, i, -1, 1, d, "SAMX")
    print(co)
