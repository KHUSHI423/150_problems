if __name__ == "__main__":
    n = int(input("Enter the number: "))
    c =1
    for i in range(n):
        for j in range(i+1):
            print(c,end=" ")
            c+=1
        print()
