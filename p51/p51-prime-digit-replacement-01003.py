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
#from _eulertools import gcd
from _tools import load_it
import operator



#lp = load_it("_list_PrimesUntil_1Mil.txt")
#l = lp[:101]
z = []
#l = [56003, 56113, 56333, 56443, 56663, 56773, 56993]
#m = [13, 23, 43, 53, 73, 83]


#n = len(l) - 1
#while n >= 0:
    #print(l[n] - l[n - 1])
    #n -= 1

#a = len(m) - 1
#while a >= 0:
    #print(m[a] - m[a - 1])
    #a -= 1

#for counter in range(10, 11, 10):
    #for ix, vx in enumerate(lpp[:-counter], counter):
        #print(ix, vx, lpp[ix])
        #for nr in zip(str(vx), str(lpp[ix])):
            #print(nr)

f = []
h = []
q = []
l = [x for x in range(2, 111)]
#print(l)
print("go")
for counter in range(10, len(l), 10):
    i = 0
    while i < len(l) - counter:
        print(counter, i, l[i], l[i + counter])
        h = list(str(l[i]))
        q = list(str(l[i + counter]))

        for nr, rn in zip(str(l[i]), str(l[i + counter])):
            if nr == rn:
                #print("*", end='')
                h.remove(nr)
                q.remove(nr)
                #print(nr,rn,  end=', ')

        if len(set(h)) == 1 and len(set(q)) == 1:
            #print("\nbngo: ", h, q)
            #print("")
            if l[i] not in f:
                f.append(l[i])
            if l[i + counter] not in f:
                f.append(l[i + counter])

        i += counter

print(f)
#print(lpp[0], lpp[-1])
#die = {k: len(v) for k, v in dic.items()}
#print('\n', die)
#mx = max(die.items(), key=operator.itemgetter(1))[0]
#print("\nPrime: ", mx, "consecutive primes: ", die[mx])
