from collections import deque

with open("22i.txt") as f:
    li = f.readline().strip()
    ds = []
    while li != "":
        d = {}
        q = deque()
        v = int(li)
        sv = v % 10
        c = sv
        for _ in range(2000):
            v = (v ^ (v << 6)) % 16777216
            v = (v ^ (v >> 5)) % 16777216
            v = (v ^ (v << 11)) % 16777216
            sv = v % 10
            q.append(sv - c)
            c = sv
            if len(q) == 4:
                k = (q.popleft(), q[0], q[1], q[2])
                if k not in d:
                    d[k] = sv
        ds.append(d)
        li = f.readline().strip()
    la = len(ds) - 1
    for i in range(la):
        for k, v in ds[i].items():
            if k in ds[la]:
                ds[la][k] += v
            else:
                ds[la][k] = v
    ls = list(ds[la].values())
    print(max(ls))