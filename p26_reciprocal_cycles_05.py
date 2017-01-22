# -*- coding: utf-8 -*-

from decimal import *
getcontext().prec = 50


def find_cycles(n='abcdabcd', start=0):

    n = str(n)
    #p = []
    p = ''
    ia = start
    ib = ia + 1

    while (ia < len(n) - 1) and (ib < len(n)):
        while n[ia] == n[ib]:
            #p.append(n[ia])
            #p = p + str(n[ia])
            p += str(n[ia])
            ia += 1
            ib += 1
            if ib == len(n):
                break

        else:
            ib += 1

    return p

nn = 'abcdabcda'
#print(find_cycles(nn))

for i in range(1,11):
    print(i, 1/i)
    print(find_cycles(1/i,2))
