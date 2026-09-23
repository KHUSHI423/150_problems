if __name__ == "__main__":

    integerRep = int(input("Enter the integer: "))

    highestSet = lowestSet = 0

    # Find lowest set bit
    n = integerRep
    i = 0

    while n:
        if n & 1 == 1:
            lowestSet = i
            break

        i += 1
        n >>= 1

    # Find highest set bit
    n = integerRep
    i = 0

    while n:
        highestSet = i
        i += 1
        n >>= 1

    print("Lowest set bit position:", lowestSet)
    print("Highest set bit position:", highestSet)