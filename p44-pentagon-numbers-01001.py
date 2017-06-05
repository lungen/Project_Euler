def makePentaValuesDict(n):
    d = {}
    for i in range(1, n + 1):
        v = int(((i * (3 * i - 1)) / 2))
        if v not in d:
            d[v] = v

    return d

d = makePentaValuesDict(10000)
#print(d, len(d))

for ix, ky in enumerate(d):
    for jx, ly in enumerate(d):
        #r = d[ky] + d[ly]
        if ky + ly in d and ly - ky in d:
            print("bingo", ky, ly, ky + ly, ly - ky)



print("fin")

