
z = "abc"
y = "123"

#for i, j in zip(z, y[1:]):
    #print(i, j)

a = "abcabc"

for c, v , b, in zip(a, a[1:], z):
    print(c, v, b)
