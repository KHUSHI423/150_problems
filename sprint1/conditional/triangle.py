if __name__ == "__main__":
    a,b,c = map(int,input("Enter three sides of triangle: ").split())
    if a == b and b== c:
        print("Valid - equilateral")
    elif a == b or b == c or a == c:
        print("Valid - isosceles")
    elif a != b and b != c and a != c and a + b > c and a + c > b and b + c > a:
        print("Valid - scalene")
    else:
        print("Invalid")