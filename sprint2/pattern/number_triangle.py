N = int(input())

for i in range(1, N + 1):

    # spaces
    print(" " * (N - i), end="")

    # increasing numbers
    for j in range(1, i + 1):
        print(j, end="")

    # decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()