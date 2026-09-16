if __name__ == "__main__":
    n  = int(input("enter the number: "))
    def fact(n):
        if n <=1:
            return 1
        return n*fact(n-1)
    def sum_digit(n):
        digit = 0
        while n:
            digit+= n%10
            n//=10
        return digit
    print(f"factorial of {n} :",fact(n))
    print(f"sum of digits of {n} : ",sum_digit(fact(n)))