from decimal import Decimal, getcontext
getcontext().prec = 50


def makeCycles(start, stop):
    for i in range(start, stop + 1):
        erg = Decimal(1) / Decimal(i)


def skipZero(n):
    n = str(n)
    new = str()

    i = 0
    while i < len(n):
        if n[i] == '0':
            continue
        else:
            new = new + n[i]
        i += 1

    return new

def finder(substr, astr):
    astr = str(astr)
    astr = astr[2:]
    substr = str(substr)
    indices = []

    # where to start from
    index = -1
    #index = 0
    while True:
    # find next index of substring, by starting search from index + 1
        index = astr.find(substr, index + 1)
        if index == -1:
            break  # all occurrences have been found
        indices.append(index)

    return indices

#print(finder('a', 'abcabca'))

seven = Decimal(1) / Decimal(7)
print(seven)
print(finder(1, seven))
print(skipZero('0012300123'))
