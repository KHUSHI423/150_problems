if __name__ == "__main__":
    n = int(input("Enter n: "))

    count = 0
    power = 5

    while power <= n:
        count += n // power
        power *= 5

    print("Number of trailing zeros:", count)