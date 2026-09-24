def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


n = int(input())

for p in range(2, n // 2 + 1):
    q = n - p

    if is_prime(p) and is_prime(q):
        print(f"{p}+{q}")
        break