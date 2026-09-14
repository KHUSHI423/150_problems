if __name__ == "__main__":
    n = int(input("Enter the number: "))
    sum_of_digits = sum(int(x) for x in str(n))
    if n % sum_of_digits == 0:
        print(f"{n} is a Harshad number")
    else:
        print(f"{n} is not a Harshad number")