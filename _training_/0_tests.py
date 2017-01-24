
def fu(z):
    for i in range(2, z, 1):
        if not z % i:
            erg = z / i
            print(z, i, erg)
            fu(erg)
        else:
            print("NOK: ", z, i)

fu(10)
