dnr = 1
value = 1
factors = [1]

print(dnr, value, factors)

for n in range(2, 10000):
    value += n
    dnr = n
    for f in range(2, value + 1):
        if not value%f:
            if f not in factors:
                factors.append(f)
        
    print(dnr, value, len(factors))
    
    if len(factors) > 500:
        break
        
    factors = [1]

print("OK: ", value, len(factors))
