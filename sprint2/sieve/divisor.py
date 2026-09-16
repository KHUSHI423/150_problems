if __name__ =="__main__":
    n = int(input("enter the number: "))
    def div(i):
        c =0
        for j in range(1,(int(i**0.5)+1)):
            if i%j == 0:
                c+=j
                if j != i // j:
                    c += i // j
        return c
    sum_divisor = 0       
    for i in range(1,n+1):
        sum_divisor+=div(i)
    print(sum_divisor)   