import pdb


nr ='abcabca'

n = 0

for ia, ea in enumerate(nr[1:]):

    if ea == nr[n]:
        #print("bingo")

        
        m = ia
        while m < len(nr):
            if nr[m + 1] == nr[n]:
                print("bingo 2: ", nr[m], nr[n], "m: ", m, "len(nr): ", len(nr))

                m += 1






