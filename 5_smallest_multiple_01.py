# -*- coding: utf-8 -*-
"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
----------------------------------
A: 232792560
----------------------------------
"""


li = []

for z in xrange(20, 900000000, 20):
    for u in xrange(1, 21):
        if not z % u:
            if u == 20:
                li.append(z)
            continue
        else:
            break
print(li)
