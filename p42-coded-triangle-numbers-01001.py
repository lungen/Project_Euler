"""
Coded triangle numbers
Problem 42
The nth term of the sequence of triangle numbers is given by,
tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding
to its alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the
word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English words, how many
are triangle words

p42_words.txt

"""

import operator


dt = {}
da = {}
count = 0
suma = 0


with open('p42_words.txt') as f:
    data = f.read().lower().replace('"', '').split(',')

da = {chr(j): j - 96 for j in range(97, 123)}

dt = {int(0.5 * i * (i + 1)): int(0.5 * i * (i + 1)) for i in range(1, 1000)}
#mx = max(dt.items(), key=operator.itemgetter(1))[0]

for word in data:
    for s in word:
        suma += da[s]
    if int(suma) in dt:
        #print("tri world: ", word)
        count += 1
    suma = 0

print("found: ", count)
