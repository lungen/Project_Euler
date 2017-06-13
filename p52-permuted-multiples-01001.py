"""
Permuted multiples
Problem 52

It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x,
and 6x, contain the same digits.
"""


i = 2
j = 0
k = 2
stop = False

while i <= 100000000:
    while not stop and k <= 6:
        j = i * k
        if sorted(str(i)) == sorted(str(j)):
            print("f: ", i, j, k)
            if k == 6:
                print("bngo: ", i, sorted("".join(str(i))), k)
            k += 1
        else:
            stop = True
            k = 2

    i += 1
    stop = False

print("fin", i)
