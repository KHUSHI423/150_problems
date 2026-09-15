if __name__=="__main__":
    arr = list(map(int,input("Enter the numbers: ").split()))
    arr.sort(reverse=True)
    gcd = arr[0]
    def cal_gcd(a,b):
        while b:
            a,b = b, a%b
        return a
    for i in range(1,len(arr)):
        gcd = cal_gcd(arr[i],gcd)
    print("gcd of the array is: ",gcd)