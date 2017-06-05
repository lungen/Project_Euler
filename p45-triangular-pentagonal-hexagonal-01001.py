def makeTriangle(n=1, lim=10):
    while n <= lim:
        v = (n * (n + 1)) / 2
        yield int(v)
        n += 1


def makePentagonal(n=1, lim=10):
    while n <= lim:
        v = (n * (3 * n - 1)) / 2
        yield int(v)
        n +=1


def makeHexa(n=1, lim=10):
    while n <= lim:
        v = n * ( 2 * n -1)
        yield v
        n += 1


x = 100000
t = set(makeTriangle(1, x))
#print(t)
print(len(t))

p = set(makePentagonal(1, x))
#print(p)
print(len(p))

h = set(makeHexa(1, x))
#print(h)
print(len(h))

print(t & p & h)
