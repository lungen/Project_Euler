def euler32():
    v = list("123456789")
    r = set()
    for a in range(2, 100):
        for b in range(a + 1, 10000):
            s = str(a) + str(b) + str(a * b)
            n = len(s)
            if n > 9:
                break
            elif n < 9 or sorted(s) != v:
                continue
            else:
                r.add(a * b)
    return sum(r)


print(euler32())
