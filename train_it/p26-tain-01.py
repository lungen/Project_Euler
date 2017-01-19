def start(z):

    for ix, vx in enumerate(z[:-1]):
        #print(vx)

        for iy, vy in enumerate(z[ix +1 :], 9):
            print(vy, iy)












#z = "123123"
z = "abcabc"

start(z)
