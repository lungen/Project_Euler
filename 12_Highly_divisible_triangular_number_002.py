value = 1
factors = [1]

for n in range(2, 1000000):
    value += n
    for f in range(2, value + 1):
        if not value % f:
            factors.append(f)

    if len(factors) > 500:
        break

    factors = [1]

print("OK: ", value, len(factors))
