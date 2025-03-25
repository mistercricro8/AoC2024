with open("22i.txt") as f:
    li = f.readline().strip()
    s = 0
    while li != "":
        v = int(li)
        for _ in range(2000):
            v = (v ^ (v << 6)) % 16777216
            v = (v ^ (v >> 5)) % 16777216
            v = (v ^ (v << 11)) % 16777216
        s += v
        li = f.readline().strip()
    print(s)