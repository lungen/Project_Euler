# -*- coding: utf-8 -*-


def make_divi(n):

    divi = [i for i in range(1, n) if not n % i]
    s = list(map(int, divi))
    return sum(s)


def loop_it(start=2, limit=5):

    total = 0
    for r in range(start, limit + 1):
        sum1 = make_divi(r)
        if r != sum1:
            sum2 = make_divi(sum1)
            if r == sum2:
                total += r
                print("GOT IT: ", r, sum1, sum2, total)




def start():

    loop_it(1, 10000)


start()
