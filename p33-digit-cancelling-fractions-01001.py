"""
Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly
believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominato
"""

import time

startTime = time.strftime("%H:%M:%S")
print("go >>> ", startTime)


n = 11
d = 12
r = 0

while n <= 98:
    if not n % 10:
        n += 1

    while d <= 99:
        if not d % 10:
            d += 1

        nn = str(n)
        dd = str(d)

        if (nn[0] in dd or nn[1] in dd) and d != n:
            v0 = n / d
            #print(dd.find(nn[0]))
            #print(nn, "/", dd, n / d)
            if int((nn[0])) / int(dd[dd.find(nn[0])]) == v0:
                print("bgno", int((nn[0])), "/", int(dd[dd.find(nn[0])]), v0, dd[dd.find(nn[0])])
                print(n, d)
            #print("bgno: ", int(nn[0]), "/", int(dd[0]), v0, \
                    #n, d)




        d += 1
    n += 1
    d = n + 1





endTime = time.strftime("%H:%M:%S")
print("start: ", startTime, ">>>", endTime)
