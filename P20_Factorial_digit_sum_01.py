def start(n):
    suma = n
    for nr in range(n, 0, -1):
        suma *= nr 
    s = str(suma)
    ssuma = list(map(int, s))
    print(sum(ssuma))
start(100)
