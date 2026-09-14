if  __name__== "__main__":
    n = int(input("Enter the number of rows: "))
    for i in range(n, 0, -1):
        for k in range(n - i):
            print(" ", end="")
        for j in range(i):
            print("*", end="")
        
        print()