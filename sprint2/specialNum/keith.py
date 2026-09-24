def is_keith(n):
    digits = list(map(int, str(n)))
    d = len(digits)

    seq = digits[:]

    while True:
        next_term = sum(seq[-d:])

        if next_term == n:
            return True

        if next_term > n:
            return False

        seq.append(next_term)


n = int(input())

if is_keith(n):
    print("Keith Number")
else:
    print("Not Keith Number")