# -*- coding: utf-8 -*-

#n = 'abcabcabcabcabcabcabcabcabcabcabcabc'
n = 'abcdabcd'
len_n = len(n)
n_seven = n[6]

p = []


break_it = False

ia = 0
ib = 1

# while ia < len(n) -1 and not break_it:
while ia < len(n) -1 and ib < len(n):

    while n[ia] == n[ib]:
        p.append(n[ia])
        print(n[ia])
        ia += 1
        ib += 1
        if ib == len(n):
            ia = len(p)
            break
            #break_it = True

    else:
        ib += 1
        #if ib == len(n):
            #break_it = True


