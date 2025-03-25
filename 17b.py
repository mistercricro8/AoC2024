def gc(ra, rb, rc, v):
    if v == 4:
        return ra
    if v == 5:
        return rb
    if v == 6:
        return rc
    return v


with open("17i.txt") as f:
    f.readline()
    irb = int(f.readline().split()[2])
    irc = int(f.readline().split()[2])
    f.readline()
    p = [int(x) for x in f.readline()[9:].split(",")]

cds = [0]
for i in range(len(p) - 1, -1, -1):
    es = p[i:]
    ncds = []
    for cd in cds:
        for ira in range(cd, cd + 8):
            pc = 0
            s = []
            ra = ira
            rb = irb
            rc = irc
            while pc < len(p):
                li = p[pc + 1]
                co = gc(ra, rb, rc, li)
                if p[pc] == 0:
                    ra = ra // (2**co)
                elif p[pc] == 1:
                    rb = rb ^ li
                elif p[pc] == 2:
                    rb = co % 8
                elif p[pc] == 3:
                    if ra != 0:
                        pc = li
                        continue
                elif p[pc] == 4:
                    rb = rb ^ rc
                elif p[pc] == 5:
                    s.append(co % 8)
                    if s[len(s) - 1] != es[len(s) - 1]:
                        break
                elif p[pc] == 6:
                    rb = ra // (2**co)
                elif p[pc] == 7:
                    rc = ra // (2**co)
                pc += 2
            j = 0
            while j < len(s) and j < len(p) and s[j] == es[j]:
                j += 1
            if j == len(es):
                ncds.append(ira * 8)
    cds = ncds
print(min(cds) // 8)
