import sys
sys.setrecursionlimit(9000)


def dividor(z, n, declist, loop=10):
    if loop == 0:
        return declist
    else:
        rest = (z % n) * 10
        dec = z // n
        declist += str(dec)

        return dividor(rest, n, declist, loop - 1)


def massband(s, dif=-1):
    i = 0

    if dif == -1:
        j = i + 1
    else:
        j = dif

    if len(s) <= (2 * dif):
        return s[:dif]
    else:
        while i < len(s):
            while j < len(s):
                if s[i] == s[j]:
                    dif = j - i
                    k = j
                    if (dif + k) >= len(s):
                        break
                    while s[k] == s[dif + k]:
                        k += dif
                        if k > (len(s) / 10):
                            return massband(s[i + 1:], dif)
                j += 1
            i += 1
            j = i + 1


def loopRec():

    maxi, maxlen = 0, 0

    for i in range(1, 1001):
        res = dividor(1, i, declist='', loop=2000)
        res = str(res)
        n = massband(res[2:-2])
        if n:
            if len(n) > maxi:
                maxi = len(n)
                maxlen = i

    print("i: {0}, len: {1} ".format(maxlen, maxi))


loopRec()
