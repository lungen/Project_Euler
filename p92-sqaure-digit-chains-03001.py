"""
VERSION WITH TWO DICTs
"""
from time import ctime

print("----------> START: {0}".format(ctime()))
d1 = {}
d89 = {}

d1[1] = 1
d89[89] = 89

c1 = 0
c89 = 0

for i in range(1, 10000001):

    if i in d1:
        c1 += 1
        continue

    if i in d89:
        c89 += 1
        continue

    sL = []
    aL = []
    stop = False
    new = i
    while (new != 1) and (new != 89) and not stop:
        sL = list(str(new))
        new = sum([int(x) * int(x) for x in sL])

        if new in d1:
            aL.append(i)
            c1 += 1
            new = 1
            stop = True

        if new in d89:
            aL.append(i)
            c89 += 1
            new = 89
            stop = True

        if not stop:
            aL.append(new)

    else:
        if new == 1:
            for m in aL:
                d1[m] = 1
        elif new == 89:
            for m in aL:
                d89[m] = 89
        else:
            print("FCUK", new, i)

#print(d1.keys())
#print(d89.keys())
print(len(d1))
print(len(d89))
print(c1)
print(c89)
print("total: ", c1 + c89)
print("----------> END: {0}".format(ctime()))
