"""
SLIM VERSION - ONE DICT
"""
from time import ctime

print("----------> START: {0}".format(ctime()))


def sqt(n):
    print(n % 10)


def run():
    d = {}
    d[1] = 1
    d[89] = 89

    for i in range(1, 10000001):

        if i in d:
            continue

        sL = []
        aL = []
        stop = False
        new = i
        while (new != 1) and (new != 89) and not stop:
            sL = list(str(new))
            new = sum([(int(x) ** 2) for x in sL])

            if new in d:
                aL.append(i)
                stop = True

            if not stop:
                aL.append(new)

        else:
            if d[new] == 1:
                for m in aL:
                    d[m] = 1
            elif d[new] == 89:
                for m in aL:
                    d[m] = 89
            else:
                print("FCUK", new, i)

    print("len of dict: ", len(d))
    sum1 = sum(a == 1 for a in d.values())
    print("Sum of 1s: ", sum1)
    sum2 = sum(a == 89 for a in d.values())
    print("\nFinally sum of 89s: ", sum2)


sqt(11)

print("----------> END: {0}".format(ctime()))
