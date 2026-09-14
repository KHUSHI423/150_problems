if __name__ == "__main__":
    n = int(input("Enter the number: "))
    original_n = n
    l = len(str(n))
    val = 0
    while n > 0:
        digit = n % 10
        val = val + digit**l
        
        n //= 10
    if val == original_n:
        print("The number is an Armstrong number.")
    else:
        print("The number is not an Armstrong number.")
        
