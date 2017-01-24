#n = 'abcabcabcabcabcabcabcabcabcabcabcabc'
n = 'abcDFG123'
len_n = len(n)
n_seven = n[6]

p = []

BREAKIT = True

ia = 0
ib = 1

while ia < len(n) -1 and BREAKIT: 
    
        while n[ia] == n[ib]:
            p.append(n[ia])
            print(n[ia])
            ia += 1
            ib += 1
            if ib == len(n):
                ia = len(p)
                BREAKIT = False
                break
        else:
            ib += 1
            if ib == len(n):
                BREAKIT = False
        
