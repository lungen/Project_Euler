"""
Prime digit replacements
Problem 51

By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the
same digit, this 5-digit number is the first example
having seven primes among the ten generated numbers,
yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the
number (not necessarily adjacent digits) with the same
digit, is part of an eight prime value family.
"""
"""
brainstorming:

    0   x   o   o
    1   x   o
    2       o   o   o
    3   x   o   o   o
    4   x   o   o   o
    5       o       o
    6   x   o   o   o
    7   x       o   o
    8           o   o
    9   x   o   o   o

        7   8   8   8

orginal     possible

56003       50603
56113       51613
56333       53633
56443       54643
56663       56663
56773       57673
56993       59693




Number has to start between 0 - 3, f.e:
    00, 11, 22, 33
    000, 111, 222, 3333

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit, is part of an eight
prime value family.


search for a number with mutliples 0, 1, 2, or 3s:
    56003 => 00

replace the 00 with 11, search for number with replacement:
    56113

replace number with 22, search for number with replacement:
    56223

etc.
"""

from _tools import load_it
def isPrime(x):
    n = abs(int(x))

    if n < 2:
        return False
    if n == 2:
        return True

    # check if even number
    if not n & 1:
        return False

    for i in range(3, int((n ** 0.5)) + 1, 2):
        if not n % i:
            return False

    return True


primList = set(load_it('/home/alkk/Project_Euler/_list_PrimesUntil_1Mil.txt'))
print("len primList: ", len(primList))
#print("last prim: ", primList[-1])


def familyTree(n, end, d, maxCount):
    # familyTree(20021, len(str(20021)), 0, 2)
    # lenD = 2 => 00
    # lenD = 3 => 000
    # 20021 -> 21121
    count = 0
    if len(str(n)) > end:
        return

    s = str(n)
    copy = list(s)
    f = s.find(str(d))
    while f != -1:
        count += 1
        copy[f] = str(d + 1)
        f = s.find(str(d), f + 1)
    else:
        # no match, continue with next number
        if count == 0:
            continue
        else:
            







maxCount = 2
for i in range(20013, 22222, 2):
    # check if is a prime number
    if isPrime(i):
        count = 0
        # check if number hast multiples digits: 00, 11, 22, 33
        s = str(i)
        copy = list(s)
        f = s.find('0')
        while f != -1:
            count += 1
            copy[f] = '1'
            f = s.find('0', f + 1)
        else:
            if count >= maxCount:
                #maxCount = max(maxCount, count)
                copy = "".join(copy)
                if copy in primList:
                    print(maxCount, i, copy)
            continue
