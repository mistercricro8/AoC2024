with open("8i.txt") as f:
    fr = {}
    l = f.readline()
    i = 0
    w = len(l)-1
    while l != "":
        for j in range(w):
            if l[j] != ".":
                if l[j] not in fr:
                    fr[l[j]] = [(i, j),]
                else:
                    fr[l[j]].append((i, j))
        i += 1
        l = f.readline()
    h = i

a = set()
for k in fr.keys():
    for n1 in fr[k]:
        for n2 in fr[k]:
            if n1 == n2:
                continue
            a.add(n2)
            di = n2[0] - n1[0]
            dj = n2[1] - n1[1]
            de = (n2[0] + di, n2[1] + dj)
            while 0 <= de[0] < h and 0 <= de[1] < w:
                a.add(de)
                de = (de[0] + di, de[1] + dj)
print(len(a))