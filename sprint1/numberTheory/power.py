if __name__ == "__main__":
    b = int(input("Enter the base: "))
    e = int(input("Enter the exponent: "))
    def power(base, exponent):
        if exponent == 0:
            return 1
        return base *power(base,exponent-1)
    result = power(b, e)
    print(f"{b} raised to the power of {e} is: {result}")