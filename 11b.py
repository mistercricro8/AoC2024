def ss(me, a, i, t):
    if t == 0:
        return 1
    cc = 0
    s = str(a[i])
    k = (a[i], t,)
    if k in me:
        return me[k]
    if a[i] == 0:
        a[i] = 1
        cc += ss(me, a, i, t-1)
    elif len(s) % 2 == 0:
        h = len(s) // 2
        a[i] = int(s[:h])
        cc += ss(me, a, i, t-1)
        a.insert(i + 1, int(s[h:]))
        cc += ss(me, a, i + 1, t-1)
    else:
        a[i] *= 2024
        cc += ss(me, a, i, t-1)
    me[k] = cc
    return cc


with open("11i.txt") as f:
    t = [int(x) for x in f.read().strip().split(" ")]
cc = 0
me = {}
for s in t:
    c = [s,]
    cc += ss(me, c, 0, 75)
print(cc)
