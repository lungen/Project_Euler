"""
s = 'xxxabcabcabc'
s = 'xabbbbbb'
s = 'abacABACbacABAC'
s = 'abbaABBAabbaABBA'
s = 'abgikafgkad'
"""


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


def loop():
    from decimal import Decimal, getcontext

    getcontext().prec = 1000
    maxi, maxlen = 0, 0

    for i in range(1, 1001):
        res = Decimal(1) / Decimal(i)
        res = str(res)
        n = massband(res[2:-2])
        if n:
            if len(n) > maxi:
                maxi = len(n)
                maxlen = i

    print("i: {0}, len: {1} ".format(maxlen, maxi))


loop()
