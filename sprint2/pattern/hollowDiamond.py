n = int(input())

# Upper half including middle
for i in range(n):
    print(" " * (n - i - 1), end="")
    print(i + 1, end="")

    if i > 0:
        print(" " * (2 * i - 1), end="")
        print(i + 1, end="")

    print()

# Lower half
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1), end="")
    print(i + 1, end="")

    if i > 0:
        print(" " * (2 * i - 1), end="")
        print(i + 1, end="")

    print()