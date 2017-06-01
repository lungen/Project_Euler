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

100k	932741865
1M	932741865
2m	935642187
10M	947563218


"""

w = []
limit = 9
maxi = 0
maxa = []
sres = ''


for i in range(11, 10000000 + 1):
    k = list('123456789')
    stop = False
    j = 1

    sres = ''
    while j <= limit and not stop:
        res = i * j
        if len(str(res)) > 9:
            break

        if '0' in str(res):
            break

        for a in str(res):
            if a in k:
                k.remove(a)
                #lRes.extend(a)
                sres += a
            else:
                stop = True
                break
        if len(k) == 0 and len(sres) == 9:
            if int(sres) > maxi:
                    maxi = int(sres)
        j += 1

print(maxi, len(str(maxi)))
print("fin")
