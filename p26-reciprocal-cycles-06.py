# -*- coding: utf-8 -*-

"""
FAIL

(43, '02325581395348837209302325581')
(46, '02173913043478260869565217391')
(47, '0212')
(48, '0')
(49, '020408163')
(51, '019607843137254901960784313725490')
"""
from decimal import *
import _tools

getcontext().prec = 100


def find_cycles(n='abcdabcd', start=0):

    n = str(n)
    #p = []
    p = ''
    ia = start
    ib = ia + 1

    while (ia < len(n) - 1) and (ib < len(n)):
        while n[ia] == n[ib]:
            #p.append(n[ia])
            p += str(n[ia])
            ia += 1
            ib += 1
            if ib == len(n):
                break

        else:
            ib += 1

    return p


lista = []
for i in range(47, 51):
    res = Decimal(1) / Decimal(i)
    print(i, res)
    re = find_cycles(res, 2)
    print(i, re)
    if res:
        lista.append((i, re))
        lista.append((i, res))


_tools.remove_files('p26-erg')
_tools.save_it(lista, 'p26-erg')



