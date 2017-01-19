def explode(word="hello"):

    if len(word) == 1:
        return word
    else:
        return word[0] + ' ' +  explode(word[1:])

print(explode())


def factor(n=5):
    if  n == 1:
        return n
    else:
        return n * factor(n-1)

print(factor())


# abbbcc
def removeDups(a='aaabbccc'):
    if len(a) == 1:
        return a
    elif a[0] != a[1]:
        return a[0] + removeDups(a[1:])
    else:
        return removeDups(a[1:])

print(removeDups())

