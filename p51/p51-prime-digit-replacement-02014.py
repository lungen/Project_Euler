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


def hasImportantMultiples_Start(x):
    # the first condition: first number has to start with:
    # 199, 211
    sx = ''.join((sorted(str(x))))
    #limp = [00, 11, 22, 33, 44, 55]
    limp = [0, 1, 2, 3, 4, 5]
    multi = 1
    for p in limp:
        if multi * str(p) in sx:
            print("ipm: ", sx, multi * str(p))
            return True


def hasImportantMultiples_End(x):
    # for the final eight family search
    # 199, 211
    sx = ''.join((sorted(str(x))))
    for p in [33, 44, 55, 66, 77, 88, 99]:
        if str(p) in sx:
            print("ipm: ", sx)
            return True


# ll = [56003, 56113, 56333, 56443, 56663, 56773, 56993]

#lb = [13, 23, 43, 53, 73, 83]

la = []
d = {}
start = 11
#start = 199, 181
lim = 101
#start = 56000
#lim = 60001
stop = False

# first number has to have mutliple of 00 - 44 to reach the family
# condition
importantPattern = ('01234')
#importantPattern = ('0123456789')

print(" ------ go ------- ")

# basic iteration, every number is being called only one time
# 11, 11 + counter, 11 + 2 * counter, 
for nr in range(start, lim):
    if not isPrime(nr):
        continue

    if not hasImportantMultiples_Start(nr):
        continue

    for counter in range(10, 11, 10):
        nr0 = nr
        nr2 = nr + counter

        while len(str(nr0)) == len(str(nr2)) and nr2 <= lim:
            # check if new number is prim
            if not isPrime(nr2):
                break  # go on with next counter

            lnr = list(str(nr0))
            lnr2 = list(str(nr2))
            ln = []
            ln2 = []
            print(nr0, nr2)

            # check for family members
            # 101, 111, 121, 
            for i, (t, u) in enumerate(zip(lnr, lnr2)):
                if t == u:
                    print("f: ", i, t, u)
                else:
                    # diff: has to be greater than last one in every case
                    # 00, 11, 22
                    print('n: ', i, t, u)
                    # bug: 199 => 229; 1 != 2 => 9 > 2; break + if 
                    if t > u:
                        print('b! ', u, '<', t)
                        stop = True
                        break
                    ln.append(t)
                    ln2.append(u)

            if not stop and len(ln) == len(ln2) \
                    and len(set(ln)) == 1 \
                    and len(set(ln2)) == 1:
                print('bngo: ', nr0, nr2)

                if nr2 not in la:
                    la.append(nr2)
                if nr0 not in d:
                    d[nr0] = la
                elif nr2 not in d[nr0]:
                    d[nr0].append(nr2)

            la = []
            stop = False
            nr2 += counter

        # counter for, show results
        if len(la) > 0:
            print(nr0, la)

        # clean
        la = []
        stop = False
        #print("")

print(d)
#die = {k: len(v) for (k, v) in d.items()}
#print('\nlen die', len(die), "\n", die)
#mx = max(die.items(), key=operator.itemgetter(1))[0]
#print("\n", mx, " - ", die[mx], ": ", d[mx])

