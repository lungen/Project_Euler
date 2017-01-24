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


def findstr_cycles(n='abcabc', start=0):
    """ find pattern in string """

    n = str(n[start:])
    print(n)
    print(n.find(n[0], 1))
    print(n.index(n[0], 1))


def find_sub_in_string(n='abcabcdefa'):
    """ search for all substrings in string """

    print("GO")
    n = str(n)
    print(n)
    sub = n[0]
    start = 0
    print(n[0])
    while True:
        start = n.find(sub, start)
        if start == -1:
            return
        yield start
        #start += len(sub)
        start += 1
    print("no")



def run_it_1():

    lista = []
    for i in range(47, 51):
        res = Decimal(1) / Decimal(i)
        print(i, res)
        re = find_cycles(res, 2)
        print(i, re)
        if res:
            lista.append((i, re))
            lista.append((i, res))
    #_tools.remove_files('p26-erg')
    #_tools.save_it(lista, 'p26-erg')


def run_it_2():

    lista = []
    for i in range(47, 48):
        res = Decimal(1) / Decimal(i)
        print(i, res)
        rec = find_cycles(res, 2)
        print(i, len(str(rec)), rec)

    #_tools.remove_files('p26-erg')
    #_tools.save_it(lista, 'p26-erg')


#run_it_2()
#findstr_cycles()
print("aa")
find_sub_in_string()
print("dsf")
