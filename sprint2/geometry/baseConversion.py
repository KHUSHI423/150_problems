N, B = map(int, input().split())

digits = "0123456789ABCDEF"

if N == 0:
    print(0)
else:
    ans = []

    while N > 0:
        remainder = N % B
        ans.append(digits[remainder])
        N //= B

    print("".join(ans[::-1]))