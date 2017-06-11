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
l = []
su = 1

while n <= 98:
    if not n % 10:  # skip 10, 20, ...
        n += 1

    while d <= 99:
        if not d % 10:  # skip 10, 20, ...
            d += 1

        nn = list(str(n))
        dd = list(str(d))

        # check if nominator is in dividor:
        if (nn[0] in dd or nn[1] in dd) and nn != dd:
            v = n / d
            #print(nn, dd)

            # check which number is in dividor
            # 22
            # 29 

            # first numenator
            #if nn[0] in dd:
                ##print(nn[0], "in ", dd)
                #nnn = list(nn[1])
                #ddd = dd[:]
                #ddd.remove(nn[0])
                #v0 = int(nnn[0]) / int(ddd[0]) 
                #if v0 == v:
                    #print("new-0: ", n, d, nnn, ddd, v0, v)

            #if nn[1] in dd:
                ##print(nn[0], "in ", dd)
                #nnn = list(nn[0])
                #ddd = dd[:]
                #ddd.remove(nn[1])
                #v0 = int(nnn[0]) / int(ddd[0]) 
                #if v0 == v:
                    #print("new-1: ", n, d, nnn, ddd, v0, v)

            # 12 / 24 => 2 / 4
            for _, x in enumerate(nn):
                if x in dd:
                    nn.remove(x)
                    dd.remove(x)
                    if v == (int(nn[0]) / int(dd[0])):
                        print("     short: ", n, d, x, int(nn[0]), int(dd[0]), v, (int(nn[0]) / int(dd[0])))
                        su *= int(dd[0])
                        print("sum: ", su)





        d += 1
    n += 1
    d = n + 1





endTime = time.strftime("%H:%M:%S")
print("start: ", startTime, ">>>", endTime)
