"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit 
fractions with denominators 2 to 10 are given:

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 
1/7 has a 6-digit recurring cycle.
Find the value of d/1000 for which 1/[d] contains the longest recurring cycle in its 
decimal fraction part.
"""


import _tools


def start(l=1001):
    # length of floating point = 59

    lista = []
    maxi_lista = []
    maxi = 0
    for i in range(1, l):
        #lista.append(("{:.70}".format(1/i)))
        erg = float(1/i) 
        lista.append(erg)
        if len(str(erg)) > maxi:
            maxi = len(str(erg))
            maxi_list = [erg, i]


    print(len(lista))
    print(maxi)
    print(maxi_list)
    #_tools.save_it(lista, "p26_daten")


start()
