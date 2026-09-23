def validate(A, N):
    magic = N * (N * N + 1) // 2

    # Check numbers 1 to N² occur exactly once
    nums = [x for row in A for x in row]

    if set(nums) != set(range(1, N * N + 1)):
        return False

    # Check rows
    for i in range(N):
        if sum(A[i]) != magic:
            return False

    # Check columns
    for j in range(N):
        if sum(A[i][j] for i in range(N)) != magic:
            return False

    # Check diagonals
    if sum(A[i][i] for i in range(N)) != magic:
        return False

    if sum(A[i][N - 1 - i] for i in range(N)) != magic:
        return False

    return True


def generate(N):
    A = [[0] * N for _ in range(N)]

    row = 0
    col = N // 2

    for num in range(1, N * N + 1):

        A[row][col] = num

        nr = (row - 1) % N
        nc = (col + 1) % N

        if A[nr][nc] != 0:
            row = (row + 1) % N
        else:
            row = nr
            col = nc

    return A


# MAIN
parts = input().split()

if parts[0] == "validate":

    N = int(parts[1])

    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    if validate(A, N):
        magic = N * (N * N + 1) // 2
        print(f"Valid Magic Square, constant={magic}")
    else:
        print("Not a Magic Square")

elif parts[0] == "generate":

    N = int(parts[1])

    A = generate(N)

    print(A)