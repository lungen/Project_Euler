# -*- coding: utf-8 -*_

def read_file():
    with open("p022_names.txt", "r") as f:
        data = f.read()

    names = [name.lower() for name in data.strip().split(",")]
    return names


def abc_value(name):

    suma = 0
    for idx, string in enumerate(name):
        if string != '"':
            suma += (ord(string) - 96)
    return suma



def run_it(names):

    big_suma = 0
    for idx, name in enumerate(names):
        big_suma += abc_value(name) * (idx + 1) 
    print(big_suma)


def start():

    names = sorted(read_file())
    # abc_value("adam")
    run_it(names)

start()
