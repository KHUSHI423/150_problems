if __name__ == "__main__" :
    n,r = map(int,input("enter the values: ").split())
    def fact(x):
        if x <= 1:
            return 1
        return x*fact(x-1)
    print(fact(n)//((fact(r))*fact(n-r)))