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


def save_it(data):

    with open("P23_Abdunant_Numbers_2.txt", "w") as f:
        f.write('\n'.join(str(line) for line in data))
    print("DATA SAVED")


def make_abd_nr(n=50):

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
                    # abd_nrs.append((i, suma))
                    # print(" - BINGO - ", i, suma)
                    break
                # print(i, j, abd_div, suma)

    # print(abd_nrs)
    # save_it(abd_nrs)
    print("ABDN-Numbers made and saved!: ", len(abd_nrs))
    return abd_nrs


def check_int(data):

    inters = []
    ck_suma = 0
    for i in range(1, limit + 1):
        for idx, element in enumerate(data):
            if i not in data:
                if not i % element:  # Teilbar
                    break
                else:  # nicht teilbar
                    if i not in inters:
                        inters.append(i)
                        ck_suma += i
    # print(inters)
    print("SUMA: ", ck_suma)

# big_nr = 28123
limit = 500
abd_numbers = make_abd_nr(limit)
# print(abd_numbers)
check_int(abd_numbers)
