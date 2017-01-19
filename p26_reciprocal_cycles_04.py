# -*- coding: utf-8 -*-


def find_cycles(n='abcdabcd', start=0):

    p = []
    ia = start
    ib = ia + 1

    while (ia < len(n) - 1) and (ib < len(n)):
        while n[ia] == n[ib]:
            p.append(n[ia])
            ia += 1
            ib += 1
            if ib == len(n):
                break

        else:
            ib += 1

    return p

print(find_cycles())



