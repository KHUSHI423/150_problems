N, M, k = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

add = []
sub = []
scalar = []

for i in range(N):
    add_row = []
    sub_row = []
    scalar_row = []

    for j in range(M):
        add_row.append(A[i][j] + B[i][j])
        sub_row.append(A[i][j] - B[i][j])
        scalar_row.append(k * A[i][j])

    add.append(add_row)
    sub.append(sub_row)
    scalar.append(scalar_row)

print("A+B=" + str(add))
print("A-B=" + str(sub))
print(f"{k}×A=" + str(scalar))