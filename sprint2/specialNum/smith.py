def digit_sum(n):
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total


def is_smith(n):
    original = n
    factor_sum = 0
    factor = 2
    composite = False

    while factor * factor <= n:

        while n % factor == 0:
            composite = True
            factor_sum += digit_sum(factor)
            n //= factor

        factor += 1

    # Remaining number is a prime factor
    if n > 1:
        factor_sum += digit_sum(n)

    return composite and digit_sum(original) == factor_sum


n = int(input())

if is_smith(n):
    print("Smith number")
else:
    print("Not a Smith number")