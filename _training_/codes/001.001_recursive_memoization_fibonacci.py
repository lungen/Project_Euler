"""
Published on 31 Aug 2016
Let’s explore recursion by writing a function to generate the terms of the Fibonacci sequence.
We will use a technique called “memoization”
to make the function fast. We’ll first implement our own caching, but then we will use Python’s
builtin memoization tool: the lru_cache
decorator.

To learn Python, you can watch our playlist from the beginning:
https://www.youtube.com/watch?v=bY6m6...
"""


fibonacci_cache = {}

def fibonacci(n):

    # if value stored in cache, return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute the values
    if n == 1:
        value = 1
    elif n == 2:
        value = 2
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    #cache the value and return
    fibonacci_cache[n] = value
    return value

for i in range(1, 10000):
    print(i, ":", fibonacci(i))



