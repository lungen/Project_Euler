"""
Prime digit replacements
Problem 51
By replacing the 1st digit of the 2-digit number *3, it turns out that six
of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes among the ten
generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
"""

from _eulertools import isPrime
from _eulertools import gcd

# n >= 11
# no 11, 111, 1111 numbers

n = 11
stop = False
l = [56003, 56113, 56333, 56443, 56663, 56773, 56993]
m = [13, 23, 43, 53, 73, 83]
z = []


n = len(l) - 1
while n >= 0:
    print(l[n] - l[n - 1])
    n -= 1

a = len(m) - 1
while a >= 0:
    print(m[a] - m[a -1])
    a -= 1


b = 11
c = 1
dic = {}

while b <= 100:
    if isPrime(b):
        while c <= 100:
            e = b + c
            e = str(e)
            b = str(b)
            if len(e) > len(b):
                b = int(b)
                break
            if str(b[-1]) == str(e[-1]) and isPrime(e):
                #print("f: ", b, e, c)
                z.append(e)
                print(z)
                if b not in dic:
                    dic[b] = z
                else:
                    dic[b] = z.append(e)

            e = int(e)
            b = int(b)

            c += 1
    b += 1
    c = 1
    z = []

print(dic)
