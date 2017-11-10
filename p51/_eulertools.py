
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def isPrime(x):
    n = abs(int(x))

    if n < 2:
        return False
    if n == 2:
        return True

    # check if even number
    if not n & 1:
        return False

    for i in range(3, int((n ** 0.5)) + 1, 2):
        if not n % i:
            return False

    return True


# check if number is palindrome
def isPalindrome(n):
    n = str(n)
    nn = ''.join(reversed(n))
    if n == nn:
        return True
    else:
        return False


def is_palindrome(n):
        n = str(n)
        if n == n[::-1]:
                return True
        else:
                return False


def reverseNumber(a):
    # reverse a number
    rn = ''.join(reversed(str(a)))
    return int(rn)
