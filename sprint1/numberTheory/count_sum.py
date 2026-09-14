if __name__ == "__main__":
    n = int(input("Enter the number: "))
    sum_of_digits = sum(int(x) for x in str(n))
    
    count = len(str(n))
    print("Count of digits is:", count)
    print("Sum of digits is:", sum_of_digits)