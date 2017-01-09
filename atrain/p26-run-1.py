

def start(z):

    for ix, vx in enumerate(z[:-1]):

        for iy, vy in enumerate(z[1:]):

            if vx == vy:
                print('aha')
                
                m = 1
                n = iy + 0
                while m < len(z):
                    print('=', z[ix + m], z[iy + n], "ix, iy:", ix, iy, 'm, n: ', m, n)
                    if z[ix + m] == z[iy + m]:
                        print('bingo', z[ix + m], z[iy + m])
                        m += 1
                        n += 1

                    else:
                        break

#z = '123123'
z = 'abcabc'
start(z)
