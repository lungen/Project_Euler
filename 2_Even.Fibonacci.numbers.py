def fibo(n):
    suma = 0
    a, b = 0, 1
    for i in range(n):
        while b < 4000000:
            a, b = b, a + b
            if not (b % 2):
                suma += b
    print(b, suma)

fibo(100)
