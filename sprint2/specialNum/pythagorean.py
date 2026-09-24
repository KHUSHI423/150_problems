n = int(input())

triplets = []

m = 2

while m * m + 1 <= n:
    for k in range(1, m):
        a = m * m - k * k
        b = 2 * m * k
        c = m * m + k * k

        if c > n:
            continue

        # Ensure a < b
        if a > b:
            a, b = b, a

        triplets.append((a, b, c))

    m += 1

# Sort by a, then b
triplets.sort()

if triplets:
    print(",".join(f"({a},{b},{c})" for a, b, c in triplets))
else:
    print("None")