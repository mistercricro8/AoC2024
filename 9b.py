with open("9i.txt") as f:
    l = f.readline().strip()
a = []
df = []
ds = []
o = True
i = 0
for c in l:
    cc = int(c)
    la = len(a)
    if o:
        for k in range(cc):
            a.append(i)
        df.append([la, cc,])
        i += 1
    else:
        for _ in range(int(c)):
            a.append(-1)
        ds.append([la, cc,])
    o = not o
j = i - 1
while j >= 0:
    i = 0
    while i < len(df):
        if ds[i][0] > df[j][0]:
            break
        if ds[i][1] >= df[j][1]:
            df[j][0] = ds[i][0]
            ds[i][0] += df[j][1]
            ds[i][1] -= df[j][1]
        i += 1
    j -= 1

s = 0
for i in range(len(df)):
    ss = 0
    for j in range(df[i][0], df[i][0] + df[i][1]):
        ss += j * i
    s += ss
print(s)