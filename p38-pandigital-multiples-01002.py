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
limit = 9
maxi = 0
lmax = []

#for i in range(1, 987654321 + 1):
for i in range(13, 30 + 1):
    k = list('123456789')
    #k = list(range(1, 10))
    #print("status k: ", k)
    stop = False
    j = 1

    while j <= limit and not stop:
        res = i * j
        if '0' in str(res):
            print("0 in res: ", res)
            break
        for a in str(res):
            if a in k:
                #print("a in k: ", a, k)
                k.remove(a)
                #print("removed a from k: ", a, k)
        else:
            if int(res) > maxi:
                maxi = int(res)
                lmax.append(res)
            break

        j += 1
print(lmax, maxi)
