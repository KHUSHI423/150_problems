if __name__ == "__main__":
    n = int(input("Enter the number: "))
    i = 1
    ans = []
    while i <= n:
        if n % i == 0:
            ans.append(i)
        i += 1
    print(f"The divisors of the {n} are:", ans)