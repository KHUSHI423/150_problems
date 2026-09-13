class GCD:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute_gcd(self):
        while self.b:
            self.a, self.b = self.b, self.a % self.b
        return self.a
if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    gcd = GCD(num1, num2)
    print("GCD of", num1, "and", num2, "is:", gcd.compute_gcd())
