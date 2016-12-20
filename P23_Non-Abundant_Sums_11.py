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


import datetime


def timeStamped(fname, fmt='{fname}_%Y-%m-%d-%H-%M-%S'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)


def save_it(data, file_name):

    with open(timeStamped(file_name), "w") as f:
        f.write('\n'.join(str(line) for line in data))
    print("DATA SAVED")


def make_abd_nr(n=100):

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
    # save_it(abd_nrs, "P23_Abdunant_Numbers_3.txt")
    print("ABDN-Numbers made and saved!: ", len(abd_nrs))
    return abd_nrs


def load_it(file_name):

    try:
        with open(file_name, 'r') as f:
            data = f.read()
    except:
        print("FAIL to READ DATA!")

    data_list = [int(number) for number in data.split("\n")]
    return(data_list)


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
    save_it(inters, "P23_Abdunant_Numbers__not_divides.txt")
    print("SUMA: ", ck_suma)


def rolling(abundant_numbers):

    abnr = abundant_numbers

    start = 1
    suma = 0

    for element in abnr[3:]:
        for n in range(start, element):
            print("Suma + n:", suma, n, " = ", (suma + n))
            suma += n

        start = element + 1

    print(suma)
    print("suma + 28123: ", suma + 28123)


def make_sum(data):

    suma = []
    for idx, element in enumerate(data[:10]):
        for ndx, value in enumerate(data[:10]):
            res = element + value
            print(element, value)
            if res > 28123:
                break
            if res not in suma:
                suma.append(res)

    print(len(suma))
    save_it(suma, "P23_Sum_of_Abundant_Numbers.txt")

# big_nr = 28123
limit = 28123
# abd_numbers = make_abd_nr(limit)
# check_int(abd_numbers)
# rolling(abd_numbers)
data = load_it('P23_Abdunant_Numbers.txt')
make_sum(data)
