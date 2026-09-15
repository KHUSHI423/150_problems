if __name__ == "__main__":
    arr = list(map(int,input("Enter the numbers: ").split()))
    arr.sort(reverse=True)
    lcm = arr[0]
    def cal_lcm(a,b):
        return (a*b)//cal_gcd(a,b)
    def cal_gcd(a,b):
        while b:
            a,b = b, a%b
        return a
    for i in range(1,len(arr)):
        lcm = cal_lcm(arr[i],lcm)
    print("lcm of the array is: ",lcm)