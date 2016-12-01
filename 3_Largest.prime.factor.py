"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600 851 475 143 ?

https://de.wikipedia.org/wiki/Sieb_des_Eratosthenes
"""


def prims(x):  # primzahlen erstellen
    pz = [2]
    pz_neu = []
    Rest = []

    for n in range(3, x+1):
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


def zerlegen():
    print("\nSTART ZERLEGEN")

    def teilen(zahl):
        for i in primzahlen_liste:
            if (zahl % i) == 0:
                ergebnis = zahl / i
                print("{0:>5} {1} / {2} = {3}".format("OK", zahl, i, ergebnis))
                prim_erg.append(i)
                if ergebnis != 1:
                    teilen(ergebnis)
                else:
                    # fertig
                    return 1
            else:
                print("{0} {1}".format("NOK", zahl, i))
                continue

        print("Prim Liste: ", prim_erg)


    primzahlen_liste = prims(10)
    # zahl = 13195
    zahl = 24
    prim_erg = []
    teilen(zahl)

zerlegen()
