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

*   productivity; keyboard layout switch
    https://stackoverflow.com/questions/311244/keyboard-layout-for-international-programmers
    http://eurkey.steffen.bruentjen.eu/download.html
        test eurkey     setxkbmap eu

*   find all index of elements in list (fast) => import numpy
    https://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list

*   enumerate with zip
    https://www.saltycrane.com/blog/2008/04/how-to-use-pythons-enumerate-and-zip-to/


** numbers of 10: 100, 1000, 10000
    56 00 3     56 030
    56 11 3     56 131
    56 33 3     56 333
    56 44 3     56 434

    1001        10 001
    1111        11 111
    1221        12 221
    1331        13 331


"""

#from _eulertools import isPrime
#from _eulertools import gcd
#from _tools import load_it
import operator


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


#lp = load_it("_list_PrimesUntil_1Mil.txt")
#lpp = lp[:101]
#ll = [56003, 56113, 56333, 56443, 56663, 56773, 56993]
#lb = [13, 23, 43, 53, 73, 83]

la = []
d = {}
#start = 11
#lim = 222
start = 56000
lim = 60001
print(" ------ go ------- ")

for nr in range(start, lim):
    if not isPrime(nr):
        continue

    for counter in range(10, 101, 10):
        #print(nr, isPrime(nr), end=', ')
        nr0 = nr
        #print(nr, end='    ')
        nr2 = nr + counter
        while len(str(nr0)) == len(str(nr2)) and nr2 <= lim:
            # check if new number is prim
            if isPrime(nr2):
                lnr = list(str(nr0))
                lnr2 = list(str(nr2))

                # check for family members
                for t, u in zip(lnr, lnr2):
                    if t == u:
                        lnr[lnr.index(t)] = None
                        lnr2[lnr2.index(u)] = None

                # filter out None
                lnr = list(filter(None.__ne__, lnr))
                lnr2 = list(filter(None.__ne__, lnr2))


                # if rest are similar numbers
                # 58111  -  10 :  [58151, 58171, 58211, 58411, 58441, 
                # 58511, 58661, 58711, 58771, 58991]
                # 58 1?1
                # 58 1?1
                # 58 1?1    58111
                #           58171
                # 58 2?1    58211
                #           58411


                if len(set(lnr)) == 1 and len(set(lnr2)) == 1:
                    #print(nr2, isPrime(nr2), end=', ')
                    #print(nr2, end='    ')
                    if nr2 not in la:
                        la.append(nr2)
                    if nr0 not in d:
                        d[nr0] = la
                    elif nr2 not in d[nr0]:
                        d[nr0].append(nr2)

            #nr = nr2
            nr2 += counter

        # counter for, show results
        if len(la) > 0:
            print(nr0, la)

        # clean
        la = []
        #print("")


#print(d)

die = {k: len(v) for (k, v) in d.items()}
#print('\nlen die', len(die), "\n", die)
mx = max(die.items(), key=operator.itemgetter(1))[0]
print("\n", mx, " - ", die[mx], ": ", d[mx])
# 58111  -  10 :  [58151, 58171, 58211, 58411, 58441, 58511, 58661, 58711, 58771, 58991]


