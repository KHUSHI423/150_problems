def digit_sum(n):
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total


def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def is_perfect(n):
    if n == 1:
        return False

    total = 1
    i = 2

    while i * i <= n:
        if n % i == 0:
            total += i

            if i != n // i:
                total += n // i

        i += 1

    return total == n


def is_armstrong(n):
    original = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** digits
        n //= 10

    return total == original


def is_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        reverse = reverse * 10 + n % 10
        n //= 10

    return original == reverse


def is_happy(n):
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = digit_square_sum(n)

    return n == 1


def digit_square_sum(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10

    return total


def is_harshad(n):
    return n % digit_sum(n) == 0


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

    if n > 1:
        factor_sum += digit_sum(n)

    return composite and digit_sum(original) == factor_sum


def is_fibonacci(n):
    a, b = 0, 1

    while a <= n:
        if a == n:
            return True

        a, b = b, a + b

    return False


def collatz_length(n):
    steps = 0

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        steps += 1

    return steps


def phi(n):
    result = n
    p = 2

    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p

            result -= result // p

        p += 1

    if n > 1:
        result -= result // n

    return result


n = int(input())

print(
    f"Prime: {'Yes' if is_prime(n) else 'No'} | "
    f"Perfect: {'Yes' if is_perfect(n) else 'No'} | "
    f"Armstrong: {'Yes' if is_armstrong(n) else 'No'} | "
    f"Palindrome: {'Yes' if is_palindrome(n) else 'No'} | "
    f"Happy: {'Yes' if is_happy(n) else 'No'} | "
    f"Harshad: {'Yes' if is_harshad(n) else 'No'} | "
    f"Smith: {'Yes' if is_smith(n) else 'No'} | "
    f"Fibonacci: {'Yes' if is_fibonacci(n) else 'No'} | "
    f"Collatz length: {collatz_length(n)} | "
    f"φ({n})={phi(n)}"
)