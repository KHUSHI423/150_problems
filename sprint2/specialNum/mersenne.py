def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def is_mersenne_prime(n):
    x = n + 1
    p = 0

    # Check whether n + 1 = 2^p
    while x % 2 == 0:
        x //= 2
        p += 1

    # n + 1 must be exactly 2^p
    if x != 1:
        return False

    # p must be prime and n must be prime
    return is_prime(p) and is_prime(n)


n = int(input())

if is_mersenne_prime(n):
    print("Mersenne Prime")
else:
    print("Not Mersenne Prime")