# create a year
years = [1900]
months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
d = 1
first_sundays = []
for idx, month in enumerate(months):
    for day in range(1, month + 1):
        print("{0} {1:>5} {2:>5}".format(idx + 1, day, d))
        if day == 1 and d == 7:
            first_sundays.append((idx + 1, day, d))
            print("")
        if d == 7:
            d = 1
        else:
            d += 1

print(first_sundays)
