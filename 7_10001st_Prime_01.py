"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
"""
# A: 104743


def make_primes(n=9000000):

    Rest = []
    primes = [2]

    for i in xrange(3, n+1):
        for x, v in enumerate(primes):
            if not i % v:  # KEIN REST = TEILBAR != PRIMZAHL
                Rest.append(False)
                break
            else:  # NICHT TEILBAR => EVTL PRIMZAHL
                Rest.append(True)
                continue

        if False not in Rest:
            primes.append(i)

        Rest = []
        if len(primes) == 10001:
            print(len(primes), "GEFUNDEN: ", i)
            return

    print("FERTIG, Bereich (n) zu klein!")

print(make_primes())
