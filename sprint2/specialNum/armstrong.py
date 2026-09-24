def count_digits(n):
    count = 0

    while n > 0:
        count += 1
        n //= 10

    return count


def is_armstrong(n):
    original = n
    digits = count_digits(n)
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** digits
        n //= 10

    return total == original


n = int(input())

for i in range(1, n + 1):
    if is_armstrong(i):
        print(i, end=" ")