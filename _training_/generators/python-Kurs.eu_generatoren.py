# http://www.python-kurs.eu/python3_generatoren.php


def abc():
    yield("a")
    yield("b")
    yield("c")


gen1 = abc()

letter = next(gen1)
print(letter)
letter = next(gen1)
print(letter)
letter = next(gen1)
print(letter)
