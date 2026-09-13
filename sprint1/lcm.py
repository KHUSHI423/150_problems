class lcm:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute_gcd(self):
        a = self.a
        b = self.b
        while b:
            a, b = b, a % b
        return a

    def compute_lcm(self):
        gcd = self.compute_gcd()
        return (self.a * self.b) // gcd


if __name__ == "__main__":
    a, b = map(int, input("Enter two numbers: ").split())
    lcm_obj = lcm(a, b)
    print("LCM of", a, "and", b, "is:", lcm_obj.compute_lcm())
