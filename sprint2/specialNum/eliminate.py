n, k = map(int, input().split())

survivor = 0

for i in range(2, n + 1):
    survivor = (survivor + k) % i

print(survivor + 1)