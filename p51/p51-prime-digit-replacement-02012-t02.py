ll = [56003, 56113, 56333, 56443, 56663, 56773, 56993]
#lb = [13, 23, 43, 53, 73, 83]

# if rest are similar numbers
# 58111 - 10 : [58151, 58171, 58211, 58411, 58441,
# 58511, 58661, 58711, 58771, 58991]

#la = []
global d
d = {}
li = []
nr0 = 58111
nr2 = 58211   # 1 multi
#nr2 = 58441     # 2 multis


def check(n, m):
    # check for family members
    nr0 = n
    nr2 = m


    lnr = list(str(nr0))
    lnr2 = list(str(nr2))
    ln = []
    ln2 = []
    la = []

    print(nr0, nr2)

    for i, (t, u) in enumerate(zip(lnr, lnr2)):
        if t == u:
            print("f: ", i, t, u)
        else:
            # diff: has to be greater than last one in every case
            # 00, 11, 22
            print('n: ', i, t, u)
            if t > u:
                print('b! ', u, '<', t)
                break
            ln.append(t)
            ln2.append(u)

    if len(ln) == len(ln2) and len(set(ln)) == 1 and len(set(ln2)) == 1:
        print('bngo: ', nr0, nr2)

        if nr2 not in la:
            la.append(nr2)
        if nr0 not in d:
            d[nr0] = la
        elif nr2 not in d[nr0]:
            d[nr0].append(nr2)
    la = []
    print(d)


b = 0
c = 1
while c < len(ll):
    check(ll[b], ll[c])
    b = c
    c += 1
