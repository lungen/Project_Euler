s = ''
si = '' 
v = 1

for i in range(1, 1000000):
    s += str(i)

print(len(s))

x = 1
for idx, elm in enumerate(s):
    if idx == x - 1:
        x = x * 10
        si += str(elm)
        v *= int(elm)

print(len(si))
print(v)

