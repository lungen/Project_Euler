def eulerQuadraticPrimesFormula(n):
    ''' 0 <= n <= 39 '''

    if n <= 39:
        return (n*n) + n + 41
    else:
        return 0


def incredibleFormula(n):
    ''' 0 <= n <= 79 '''

    if n <= 79:
        return (n*n) - 79 * n + 1601
    else:
        return 0


def quadraticsForm(n, a, b):
    if a < 1001 and b <= 1000:
        return (n*n) + a*n + b
    else:
        return 0


print("n² + n + 41")
for i in range(0, 41):
    print(i, eulerQuadraticPrimesFormula(i), end=', ')

print("\n\nn² -79n + 1601")
for i in range(0, 80):
    print(i, incredibleFormula(i), end=', ')

print("\n\nn² + an + b")
i, a, b = 0, 0, 0
while i < 10:
    print(i, quadraticsForm(i, a, b), end=', ')
    i += 1
    a += 1
    b += 1
