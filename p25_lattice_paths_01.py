# -*- coding: utf-8 -*-

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

zaehler = factorial(40)
nenner1 = factorial(20)
nenner2 = factorial(20)

print(zaehler / (nenner1 * nenner2))
