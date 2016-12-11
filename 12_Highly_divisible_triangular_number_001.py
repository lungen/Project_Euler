alive = 100
#  dnr = 1
value = 1
factors = [1]

print(1, value, factors)

for n in range(2, 100000000):
    value += n
    # dnr = n
    for f in range(2, value + 1):
        if not value % f:
            if f not in factors:
                factors.append(f)

    # print(n, value, len(factors))

    if len(factors) > 500:
        break

    if n == alive:
        print("Status: ", n, value, len(factors))
        alive += 500

    factors = [1]

print("OK: ", value, len(factors))
