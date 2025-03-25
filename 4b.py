def kmp(c, i, j, di, dj, n, pat, r, y):
    if n < len(pat):
        return 0
    m = 3
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
                r.append((t[0] - 2 * di, t[1] - 2 * dj, y))
                p = 0
        else:
            if p != 0:
                p = 0
            else:
                t[0] += di
                t[1] += dj
                cc += 1


def dd(i1, j1, i2, j2):
    return max(abs(i1 - i2), abs(j1 - j2)) + 1


with open("4i.txt") as f:
    c = f.readlines()
    l = len(c)
    r = []
    s = l - 1
    for i in range(l):
        c[i] = c[i].strip()
        d = dd(i, 0, s, s - i)
        kmp(c, i, 0, 1, 1, d, "MAS", r, True)
        kmp(c, i, 0, 1, 1, d, "SAM", r, True)
        d = dd(i, 0, 0, i)
        kmp(c, i, 0, -1, 1, d, "MAS", r, False)
        kmp(c, i, 0, -1, 1, d, "SAM", r, False)
        if i == 0:
            continue
        d = dd(s, i, i, s)
        kmp(c, 0, i, 1, 1, d, "MAS", r, True)
        kmp(c, 0, i, 1, 1, d, "SAM", r, True)
        d = dd(0, i, s - i, s)
        kmp(c, s, i, -1, 1, d, "MAS", r, False)
        kmp(c, s, i, -1, 1, d, "SAM", r, False)
    h = set(r)
    co = 0
    while len(h) > 0:
        i, j, y = h.pop()
        if (i, j, not y) in h:
            co += 1
            h.remove((i, j, not y))
    print(co)
