# -*- coding: utf-8 -*-

"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

!!!!!!!!!!!!!!!!!!!!!!!!!!!! A: 906609 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""

li = []
s = 100
e = 1000

for i in range(s, e):
    for u in range(s, e):
        p = str(i * u)
        q = "".join(reversed(p))
        if str(p) == str(q):
            if p not in li and len(p) > 5:
                li.append(p)
print("MAX Palindrome:", max(li))
