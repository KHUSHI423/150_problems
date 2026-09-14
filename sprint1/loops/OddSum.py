if __name__ == "__main__":
    a,b = map(int,input("Enter two numbers: ").split())
    odd_sum = 0
    for i in range(a,b+1):
        if i%2!=0:
            odd_sum += i
    print(f"The sum of odd numbers between {a} and {b} is: {odd_sum}")