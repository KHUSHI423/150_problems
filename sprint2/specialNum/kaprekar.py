def kaprekar(n):
    digits = []

    # Extract 4 digits
    for i in range(4):
        digits.append(n % 10)
        n //= 10

    digits.sort()

    small = 0
    large = 0

    for digit in digits:
        small = small * 10 + digit

    for digit in digits[::-1]:
        large = large * 10 + digit

    return large - small


n = int(input())

if n // 1000 == n % 10 == (n // 10) % 10 == (n // 100) % 10:
    print("Invalid (all digits are the same)")
else:
    chain = [n]
    steps = 0

    while n != 6174:
        n = kaprekar(n)
        chain.append(n)
        steps += 1

    print(f"{steps} steps: {' -> '.join(map(str, chain))}")
'''n = int(input())

if len(set(str(n))) == 1:
    print("Invalid (all digits are the same)")
else:
    steps = 0
    chain = []

    while n != 6174:
        chain.append(n)

        digits = list(f"{n:04d}")
        digits.sort()

        small = int("".join(digits))
        large = int("".join(digits[::-1]))

        n = large - small
        steps += 1

    chain.append(6174)

    print(str(steps) + " steps: " + " -> ".join(map(str, chain)))'''