def ch(i, v, d, ar):
    if i == len(ar):
        return v == d
    return ch(i + 1, v + ar[i], d, ar) or ch(i + 1, v * ar[i], d, ar) or ch(i + 1, int(str(v) + str(ar[i])), d, ar)

with open("7i.txt") as f:
    l = f.readline()
    s = 0
    while l != "":
        a = l.strip().split()
        d = int(a[0][:-1])
        ar = [int(x) for x in a[1:]]
        if ch(1, ar[0], d, ar):
            s += d
        l = f.readline()
    print(s)