if __name__ == "__main__":
    n = int(input("Enter the number: "))
    i = 1
    sum_of_divisors = 0
    while i < n:
        if n%i == 0:
            sum_of_divisors += i
        i += 1
    if sum_of_divisors == n:
        print(f"{n} is a perfect number.")
    else:
        print(f"{n} is not a perfect number.")