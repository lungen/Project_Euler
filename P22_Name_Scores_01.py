# -*- coding: utf-8 -*_

def read_file():
    with open("p022_names.txt", "r") as f:
        data = f.read()

    names = [name for name in data.strip().split(",")]
    return names

def start():

    names = read_file()
    print(len(names))
    print(names[0], names[-1])

    snames = sorted(names)
    print(snames[0], snames[-1])


start()
