# https://stackoverflow.com/questions/34706731/recursive-factorial-using-dict-causes-recursionerror#34706749


# returns a counter
def f(n, d={1: 1}):
    if n not in d.keys():
        result = 0
        if (n % 2 == 0):    # even number
            result = int(n / 2)
        else:               # odd number
            result = int((3 * n) + 1)

        # function recursion
        d[n] = 1 + f(result)
        return d[n]
    else:
        return d[n]


mx = 0
longestNumber = -1

for i in range(1, 1000000):
    if f(i) > mx: longestNumber, mx = i, f(i)

print("max i: ", longestNumber, "len: ", mx)
