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
while n <= 28:
    if not n % 10:  # skip 10, 20, ...
        n += 1

    while d <= 39:
        if not d % 10:  # skip 10, 20, ...
            d += 1

        nn = list(str(n))
        dd = list(str(d))

        # check if nominator is in dividor:
        if nn[0] in dd or nn[1] in dd:
            v = n / d
            print(nn, dd)

            # check which number is in dividor
            # 22
            # 29 

            if nn[0] in dd:
                #print(nn[0], "in ", dd)
                nnn = list(nn[1])
                ddd = dd[:]
                ddd.remove(nn[0])
                v0 = int(nnn[0]) / int(ddd[0]) 
                print("new-0: ", nnn, ddd, v0, v)

            #if nn[1] in dd:
                ##print(nn[1], "in ", dd)
                #nnnn= list(nn[0])
                #dddd = [x for x in dd if x != nn[1]]
                ##dd.remove(nn[1])
                #print("new-1: ", nnnn, dddd)



                


        d += 1
    n += 1
    d = n + 1





endTime = time.strftime("%H:%M:%S")
print("start: ", startTime, ">>>", endTime)
