def divisor_sum(n):
    total = 1

    if n == 1:
        return 0

    i = 2

    while i * i <= n:
        if n % i == 0:
            total += i

            if i != n // i:
                total += n // i

        i += 1

    return total


n = int(input())

partner = divisor_sum(n)

if partner != n and divisor_sum(partner) == n:
    print(f"Amicable pair: ({n}, {partner})")
else:
    print("Not amicable")