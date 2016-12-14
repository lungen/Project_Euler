# -*- coding: utf-8 -*-


def fibo(n=22):
    a, b = 0, 1
    for n in range(2, n + 1):
        a, b = b, a+b
        if len(str(b)) == 3:
            print(n, b)
            break

fibo()
