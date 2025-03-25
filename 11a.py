with open("11i.txt") as f:
    t = [int(x) for x in f.read().strip().split(" ")]
for _ in range(25):
    i = 0
    while i < len(t):
        s = str(t[i])
        if t[i] == 0:
            t[i] = 1
        elif len(s) % 2 == 0:
            h = len(s) // 2
            t[i] = int(s[:h])
            t.insert(i + 1, int(s[h:]))
            i += 1
        else:
            t[i] *= 2024 
        i += 1
print(len(t))