# -*- coding: utf-8 -*-


def fibo(n=12):
    a, b = 0, 1
    print("1 ",b)
    for n in range(2, n + 1):
        a, b = b, a+b
        print(n, b)

fibo()
