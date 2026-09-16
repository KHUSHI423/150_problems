if __name__ == "__main__":
    b,e,m=map(int,input("enter the values: ").split())
    ans = 1
    while e:
        ans*=b 
        e-=1
    print(ans%m)

