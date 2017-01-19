"""
Published on 31 Aug 2016
Let’s explore recursion by writing a function to generate the terms of the Fibonacci sequence.
We will use a technique called “memoization”
to make the function fast. We’ll first implement our own caching, but then we will use Python’s
builtin memoization tool: the lru_cache decorator.

To learn Python, you can watch our playlist from the beginning:
https://www.youtube.com/watch?v=bY6m6...
"""


from functools import lru_cache

@lru_cache(maxsize=10000)
def fibonacci(n):

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(1, 1000):
    print(i, ":", fibonacci(i))
