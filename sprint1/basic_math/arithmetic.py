class ArithmeticOperations:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def calculate(self):
        print("Sum =", self.A + self.B)
        print("Diff =", self.A - self.B)
        print("Product =", self.A * self.B)
        print("Quotient =", self.A // self.B)

    def swap_with_temp(self):
        temp = self.A
        self.A = self.B
        self.B = temp

    def swap_without_temp(self):
        self.A = self.A + self.B
        self.B = self.A - self.B
        self.A = self.A - self.B

    def display(self):
        print("A =", self.A, "B =", self.B)





if __name__ == "__main__":
    a, b = map(int, input("Enter A and B: ").split())
    
    obj = ArithmeticOperations(a, b)

    obj.calculate()

    obj.swap_with_temp()
    obj.display()

    obj.swap_without_temp()
    obj.display()