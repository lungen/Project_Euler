"""
Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""


def make_abd_nr(n):
    # make abundant numbers

    abd_nrs = []
    for i in range(n + 1):
        abd_div = []
        suma = 0
        for j in range(1, n):
            if j >= i:
                break
            if not i % j:
                abd_div.append(j)
                suma += j
                if suma > i:
                    abd_nrs.append(i)
                    break

    return abd_nrs


def make_sum(data):
    # make sum of two abundant numbers

    suma = []
    for idx, element in enumerate(data):
        for ndx, value in enumerate(data):
            res = element + value
            if res > 28123:
                break
            if res not in suma:
                suma.append(res)

    return suma


def make_sum_of(data):
    # make sum of positive integers which cannot be written as the sum
    # of two abundant numbers.

    nat_data = [int(i) for i in range(1, limit + 1)]
    set_nat_data = set(nat_data)
    set_data = set(data)
    rest_data = set_nat_data - set_data

    return rest_data


print("GO")
limit = 28123
abd_numbers = make_abd_nr(limit)
sum_of = make_sum(abd_numbers)
rest = make_sum_of(sum_of)
print(sum(rest))
