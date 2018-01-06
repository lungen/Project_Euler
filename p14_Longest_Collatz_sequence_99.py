global d
d = {}

# returns a counter
def f(n):
    # END-CONDITON
    if n == 1:
        d[n] = 1
        return 1

    # RECURSION-INIT
    if n not in d.keys():
        result = 0
        if (n % 2 == 0):    # even number
            result = int(n / 2)
        else:               # odd number
            result = int((3 * n) + 1)
# add new key
        d[n] = result
        # function recursion
        return 1 + f(result)

    # JUST A COUNTER
    else:
        # print all keys
        counter = 0
        while (n in d.keys()):
            counter += 1
            if n == 1:
                return counter
            n = d[n]
        else:
            print("fck -> n: ", n, "len(d): ", len(d))
            return 1 + f(n)


mx = 0
longestNumber = -1

for i in range(1, 1000000):
    if f(i) > mx:
        longestNumber = i
        mx = f(i)
    #print(i, f2(i))

print("max i: ", longestNumber, "len: ", mx)
