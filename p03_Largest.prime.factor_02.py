"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600 851 475 143 ?

https://de.wikipedia.org/wiki/Sieb_des_Eratosthenes

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        A: 6857
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
01.12.2016
FCK YEAH!
"""


def prims(x):  # primzahlen erstellen
    pz = [2]
    pz_neu = []
    Rest = []

    for n in xrange(3, x+1):
        for i, v in enumerate(pz, 3):
            if not n % v:  # = 0
                Rest.append(False)
                break

            if n % v:  # != 0
                if n not in pz_neu:
                    pz_neu.append(n)
                    Rest.append(True)

        if False not in Rest:
            pz.extend(pz_neu)

        # print(pz)
        Rest = []
        pz_neu = []

    return pz


def prims_teiler(zahl):
    zl = [zahl]
    primzahlen_liste = set(prims(10000))
    prim_erg = []

    for i, v in enumerate(zl):
        for j in primzahlen_liste:
            if not v % j:
                erg = v / j
                prim_erg.append(j)
                zl.append(erg)
                print(v, j ,erg)
                if erg == 1:
                    return prim_erg
                break
    print(prim_erg, zl)

super_number = 600851475143

print(prims_teiler(super_number))
