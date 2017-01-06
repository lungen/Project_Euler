
"""
A permutation is an ordered arrangement of objects. For example,
3124 is one possible permutation of the digits 1, 2, 3 and 4. If all
of the permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
 style="text-align:center;">012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2,
3, 4, 5, 6, 7, 8 and 9?
"""


def start(n):

    # 1.step find biggest P[x] and RETURN the POSITION x
    # RETURN -1 if there is not such P[x]: could be the last permutation
    largest_x = -1
    for ix, va in enumerate(n[:-1]):
        if n[ix] < n[ix + 1]:
            largest_x = ix
    if largest_x == -1:
        print(n)
        return -1


    # 2. step: find the biggest P[y] and RETURN the POSITION y
    largest_y_list = []
    for iy, vb in enumerate(n[largest_x + 1:], start=largest_x + 1):
        if n[iy] > n[largest_x]:
            largest_y_list.append(vb)
    largest_y = n.index(min(largest_y_list))


    # 3. step: replace P[x] and P[y]
    nn = n[:]
    nn[largest_x], nn[largest_y] = n[largest_y], n[largest_x]


    # 4. step: sort from postion x+1 in ascending order
    nnA = nn[:largest_x + 1]
    nnB = nn[largest_x + 1:]
    nn = nnA + sorted(nnB)
    return(nn)
    

def cycle(lista):
    
    count = 1
    # -1 means that the start-function has finished
    while lista != -1:
        if count == 1000000:
            print("FIN: ", count, lista)
            return
        lista = start(lista)
        count += 1
    else:
        print("Permutation finished.")
            
cycle([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

