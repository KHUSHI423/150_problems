def reverse_num(n):
    rev = 0

    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10

    return rev


def is_palindrome(n):
    return n == reverse_num(n)


n = int(input())

for step in range(1, 51):
    n = n + reverse_num(n)

    if is_palindrome(n):
        if step == 1:
            print(f"Not Lychrel (palindrome {n} in 1 step)")
        else:
            print(f"Not Lychrel (palindrome {n} in {step} steps)")
        break
else:
    print("Likely Lychrel (no palindrome in 50 steps)")