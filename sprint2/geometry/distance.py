import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1

# Euclidean distance
euclidean = math.sqrt(dx * dx + dy * dy)

# Manhattan distance
manhattan = abs(dx) + abs(dy)

print(euclidean)
print(manhattan)