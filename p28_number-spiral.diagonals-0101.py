def numberSpiralDiagonal(n=1001):

    i = 1
    j = 3
    m = 2
    # offset
    os = 0
    suma = 0
    sumc = 0

    while j <= n:
        suma += sum(range(i * i + os, j * j + 1, m))
        i += 2
        j += 2
        m += 2
        os = m

    if not n % 2:
        sumc = (n * n) - (n - 1)
        suma = suma + sumc

    return suma


print(numberSpiralDiagonal())
