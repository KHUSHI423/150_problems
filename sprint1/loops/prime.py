if __name__ == "__main__":
    a,b= map(int,input("Enter two numbers: ").split())
    while a<=b:
        for i in range(2,a):
            if a%i==0:
                break
        else:
            print(a,end=" ")
        a+=1