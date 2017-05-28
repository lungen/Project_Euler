import _tools

data = _tools.load_it("primes1.txt")
data2 = _tools.load_it("primes2.txt")
data3 = _tools.load_it("primes3.txt")
data4 = _tools.load_it("primes4.txt")
data5 = _tools.load_it("primes5.txt")
data6 = _tools.load_it("primes6.txt")
data7 = _tools.load_it("primes7.txt")
data8 = _tools.load_it("primes8.txt")
data9 = _tools.load_it("primes9.txt")
data10 = _tools.load_it("primes10.txt")

l = []
for line in data:
    for n in line.split():
        #print(n, end=", ")
        l.append(n)

for line in data2:
    for n in line.split():
        #print(n, end=", ")
        l.append(n)

for line in data3:
    for n in line.split():
        #print(n, end=", ")
        l.append(n)
        
for line in data4:
    for n in line.split():
        #print(n, end=", ")
        l.append(n)
for line in data5:
    for n in line.split():
        #print(n, end=", ")
        l.append(n)
for line in data6:
    for n in line.split():
        #print(n, end=", ")
        l.append(n)
for line in data7:
    for n in line.split():
        #print(n, end=", ")
        l.append(n)
for line in data8:
    for n in line.split():
        #print(n, end=", ")
        l.append(n)
for line in data9:
    for n in line.split():
        #print(n, end=", ")
        l.append(n)
for line in data10:
    for n in line.split():
        #print(n, end=", ")
        l.append(n)

print(len(l))

_tools.save_it(l, "_listOfPrimes.txt")
