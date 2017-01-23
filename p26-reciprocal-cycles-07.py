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


def run_1():
        
    lista = []
    for i in range(1, 50):
        res = Decimal(1) / Decimal(i)
        print(i, res)
        re = find_cycles(res, 2)
        print(i, re)
        if res and res is not 0:
            lista.append((i, re))
            lista.append((i, res))

    #_tools.remove_files('p26-erg')
    #_tools.save_it(lista, 'p26-erg')


def find_substring(substring, string):
    """ find substring in string """

    indices = []
    # where to start from
    #index = -1
    index = 0

    while True:
        # find next index of substring, by starting search from index + 1
        index = string.find(substring, index + 1)
        if index == -1:
            break  # all occurrences have been found
        indices.append(index)
    return indices


def find_substring_build(substr='a', str='abcabca'):

    indices = []
    index = -1

    while index < len(str) - 1:
        index = index + 1
        if str[index] == substr:
            indices.append(index)

    return indices




#print(find_substring('a', 'abcabcda'))
#run_1()
print(find_substring_build())
