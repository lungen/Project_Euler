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

#from _eulertools import isPrime
#from _eulertools import gcd
from _tools import load_it
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
#la = [56003, 56113, 56333, 56443, 56663, 56773, 56993]
#lb = [13, 23, 43, 53, 73, 83]

la = []
d = {}
start = 100
lim = 1000
print(" ------ go ------- ")

for nr in range(11, lim):
    if not isPrime(nr):
        continue

    for counter in range(10, 100, 10):
        #print(nr, isPrime(nr), end=', ')
        nr0 = nr
        print(nr, end='    ')
        nr2 = nr + counter
        while len(str(nr)) == len(str(nr2)) and nr2 <= lim:
            # check if new number is prim
            if isPrime(nr2):
                lnr = list(str(nr))
                lnr2 = list(str(nr2))

                # check for family members
                for t, u in zip(lnr, lnr2):
                    if t == u:
                        lnr.remove(t)
                        lnr2.remove(u)

                # if rest are similar numbers
                if len(set(lnr)) == 1 and len(set(lnr2)) == 1:
                    #print(nr2, isPrime(nr2), end=', ')
                    print(nr2, end='    ')
                    if nr2 not in la:
                        la.append(nr2)
                    if nr0 not in d:
                        d[nr0] = la
                    elif nr2 not in d[nr0]:
                        d[nr0].append(nr2)

            nr = nr2
            nr2 = nr2 + counter

        # counter for
        la = []
        print("")


#print(d)

die = {k: len(v) for (k, v) in d.items()}
#print('\nlen die', len(die), "\n", die)
mx = max(die.items(), key=operator.itemgetter(1))[0]
print("\n",mx, " - ", die[mx], ": ", d[mx])
