import sys
sys.setrecursionlimit(10000)


def dividor(z, n, declist, loop=10):
    if loop == 0:
        return declist
    else:
        rest = (z % n) * 10
        dec = z // n
        declist += str(dec)

        return dividor(rest, n, declist, loop - 1)


print(len(dividor(1, 7, declist='', loop=2000)))


def dividorList(z, n, declist, loop=10):
    if loop == 0:
        return declist
    else:
        rest = (z % n) * 10
        dec = z // n
        declist.append(dec)

        return dividor(rest, n, declist, loop - 1)


#print(dividorList(1, 7, declist=list(), loop=1000))
