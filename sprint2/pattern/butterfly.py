N = int(input())

# Top half
for i in range(1, N + 1):
    ones = i
    zeros = i
    spaces = 2 * (N - i)

    print("1" * ones + " " * spaces + "0" * zeros)

# Bottom half
for i in range(N, 0, -1):
    ones = i
    zeros = i
    spaces = 2 * (N - i)

    print("1" * ones + " " * spaces + "0" * zeros)