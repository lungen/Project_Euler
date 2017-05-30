def fact(number):

    if number <=1:
        return 1
    else:
        return number * fact(number - 1)

#print(fact(5))


def explode(word="hello"):
    # hello => h e l l o

    if len(word) <= 1:
        return word
    else:
        return word[0] + ' ' + explode(word[1:])

# print(explode())


def removeDups(word="aabbbcccc"):
    # aabbbcccc => abc

    if len(word) <= 1:
        return word
    elif word[0] == word[1]:
        return removeDups(word[1:])
    else:
        return word[0] + removeDups(word[1:])

#print(removeDups())


def fibo(n=5):

    a, b = 0, 1
    i = 0
    while i <= n:
        a, b = b, a + b
        i += 1

    print(a, b)

#fibo(5)


def fibo_recursive(n):

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)

print(fibo_recursive(6))
