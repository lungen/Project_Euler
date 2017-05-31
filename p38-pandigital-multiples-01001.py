"""
Pandigital multiples
Problem 38
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is whe concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

w = []
#for i in range(1, 987654321 + 1):
for i in range(1, 100 + 1):

    if str(i) in '0':
        print("continue i: ", i)
        continue

    for m in range(1, 9):
        if str(m) in '0':
            print("continue m: ", m)
            continue

        k = list('123456789')
        kr = list('123456789')
        #k = '123456789'
        r = i * m
        if '0' in str(r):
            #print("break 0 in ", r)
            break

        # abfangen, checken ob <ergebnis> nicht multis hat
        for f in str(r):
            try:
                kr.remove(str(f))
                #print(" r check ok", f, r, kr)
            except:
                #print("break r", r, kr)
                break

        w = []
        try:
            for e in str(r):
                #print("try remove: i: {0}   m: {1}  r: {2}  k: {3}   e: {4}".
                      #format(i, m, r, k, e))
                k.remove(str(e))
                w.append(e)
                #print("REMOVED: i: {0}   m: {1}  r: {2}  k: {3}   e: {4}".
                      #format(i, m, r, k, e))
        except:
            #print("not in list: ", i, " * ", m, " = ", r, k, e)
            break
        #print("Ok, weg damit: ", i, m, r, w, k)
