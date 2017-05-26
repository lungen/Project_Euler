<<<<<<< HEAD
"""
Digit fifth powers
Problem 30
Surprisingly there are only three numbers that can be
written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44
    As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the
sum of fifth powers of their digits.
"""


=======
def digitPowersDividor(x=1634):
    """
    Digit fifth powers


       Surprisingly there are only three numbers that can be
       written as the sum of fourth powers of their digits:

         1634 = 1^4 + 6^4 + 3^4 + 4^4
         8208 = 8^4 + 2^4 + 0^4 + 8^4
         9474 = 9^4 + 4^4 + 7^4 + 4^4

       As 1 = 1^4 is not a sum it is not included.

       The sum of these numbers is 1634 + 8208 + 9474 = 19316.

       Find the sum of all the numbers that can be
       written as the sum of fifth powers of their digits.

    """

    n = x
    m = str(n)
    p = 5
    while len(m) > 0:

        n = n - int(m[:1]) ** p
        m = m[1:]

    if n == 0:
        print("ok: ", n, x)
        return x
    else:
        # print("nok: ", n)
        return 0


suma = 0
for i in range(999999, 9, -1):
    suma = suma + int(digitPowersDividor(i))

print("fin: ", suma)
>>>>>>> f3c10f58387a00c81a288529fb1af27a8d925b0e
