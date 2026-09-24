N = int(input())

num = 1

for i in range(1, N + 1):

    row = []

    for j in range(i):
        row.append(num)
        num += 1

    if i % 2 == 0:
        row.reverse()

    print(row)