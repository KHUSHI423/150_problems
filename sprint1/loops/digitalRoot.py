if __name__ == "__main__":
    n = int(input("Enter the number: "))
    while n >= 10:
        sum_of_digits = 0
        while n > 0:
            digit = n % 10
            sum_of_digits += digit
            n //= 10
        n = sum_of_digits
    print("The digital root is:", n)