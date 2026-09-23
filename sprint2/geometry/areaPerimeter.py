import math

PI = 3.14159

shape = input()

if shape == "circle":
    r = float(input())
    area = PI * r * r
    perimeter = 2 * PI * r
    print(area, perimeter)

elif shape == "rectangle":
    l, w = map(float, input().split())
    area = l * w
    perimeter = 2 * (l + w)
    print(area, perimeter)

elif shape == "triangle":
    a, b, c = map(float, input().split())
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    perimeter = a + b + c
    print(area, perimeter)