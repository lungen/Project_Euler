"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

https://de.wikipedia.org/wiki/Sieb_des_Eratosthenes
"""

# primzahlen erstellen
def prims(x):
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

print(prims(5000))
