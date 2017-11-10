"""
A number chain is created by continuously adding the square of the digits in a
number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless
loop. What is most amazing is that EVERY starting number will eventually
arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
from time import ctime


fail = []
eleminator89 = {}
eleminator1 = {}
counter = 0
counter1 = 0
print("----------------------- START -------------------------")
print(ctime())
#for i in range(1, 45):
for i in range(1, 10000001):

    if i in eleminator1:
        counter1 += 1
        continue

    if i in eleminator89:
        counter += 1
        continue

    new = i
    eL = []
    while (new != 1) and (new != 89):
        eL.append(new)
        li = list(str(new))
        new = sum([int(i) * int(i) for i in li])
    else:
        if new != 1 and new != 89:
            fail.append((i, new))
        if new == 89:
            for x in eL:
                if x not in eleminator89:
                    eleminator89[x] = True
            counter += 1
        elif new == 1:
            for x in eL:
                if x not in eleminator1:
                    eleminator1[x] = True
            counter1 += 1
        else:
            pass

print("\n")
print("fail: ", len(fail), "\n")
print("len of eleminator1: ", len(eleminator1))
print("len of eleminator89: ", len(eleminator89))
print("counter of 1: ", counter1)
print("counter of 89: ", counter)
print("counter total: ", counter + counter1, "\n")
print(ctime())
#print(eleminator89.keys(), "\n")
#print(eleminator1.keys())
