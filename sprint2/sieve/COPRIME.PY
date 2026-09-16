if __name__ =="__main__":
    n = int(input("enter the number: "))
    def gcd(i,n):
        while i:
            n,i = i,n%i
        return n
        
    for i in range(1,n):
       if gcd(i,n) == 1:
          print(i,end =" ")
   