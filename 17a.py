def gc(ra, rb, rc, v):
    if v == 4:
        return ra
    if v == 5:
        return rb
    if v == 6:
        return rc
    return v


with open("17i.txt") as f:
    ra = int(f.readline().split()[2])
    rb = int(f.readline().split()[2])
    rc = int(f.readline().split()[2])
    f.readline()
    p = [int(x) for x in f.readline()[9:].split(",")]
pc = 0
s = ""
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
        s += str(co % 8) + ","
    elif p[pc] == 6:
        rb = ra // (2**co)
    elif p[pc] == 7:
        rc = ra // (2**co)
    pc += 2
print(s[:-1])
