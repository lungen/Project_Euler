# -*- code: utf-8 -*-
"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
"""

li = []

# for z in li:
for z in xrange(20, 900000000, 20):
    for u in xrange(1, 21):
        if not z % u:
            if u == 20:
                li.append(z)
            # print("{0:>5}   {1} % {2} = {3}".format("OK", z, u, (z % u)))
            # li.append((z, u, z%u))
            continue
        else:
            # print("{0:>5}   {1} % {2} = {3}".format("NOK", z, u, (z % u)))
            break
print(li)
