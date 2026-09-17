if __name__ == "__main__":
    num = int(input("enter the number: "))
    triangle = []
    square = []
    pentagonal = []
    for n in range(1,num+1):
        triangle.append((n+1)*n//2)
        square.append(n**2)
        pentagonal.append((n*(3*n - 1))//2)
    print("square :",square)
    print("Triangle :",triangle)
    print("pentagonal :",pentagonal)