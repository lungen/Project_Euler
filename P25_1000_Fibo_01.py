# -*- coding: utf-8 -*-


def fibo(n=100000):
    a, b = 0, 1
    for n in range(2, n + 1):
        a, b = b, a+b
        if len(str(b)) == 1000:
            print(n, b)
            break

fibo()
