# -*- coding: utf-8 -*-
"""
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
maxx = 0
li = []
maxli = []
maxterms = []

for i in range(2, 1000001):
    li.append(i)

    for m in li:
        if not m % 2:
            m = m/2
        else:
            m = 3 * m + 1

        if m == 1:
            li.append(m)
            if len(li) > maxx:
                maxx = len(li)
                maxli = i
                maxterms = li[:]
            li[:] = []
            break  # next number i

        else:
            li.append(m)

print("- FINISHED - Max Number: {0} {1:10}[LEN]".format(maxli, maxx))
