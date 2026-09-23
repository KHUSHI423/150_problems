N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

T = []

for j in range(M):
    row = []

    for i in range(N):
        row.append(A[i][j])

    T.append(row)

print(T)