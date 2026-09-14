class Fibonacci:
    def __init__(self,n):
        self.n = n
    def fib(self):
        a = 0
        b = 1
        sequence = []
        for i in range(self.n):
            sequence.append(a)
            a, b = b, a + b
        return sequence

if __name__ == "__main__":
    n = int(input("enter the number: "))
    obj = Fibonacci(n)
    print("Fibonacci sequence is: ")
    for x in obj.fib():
        print(x, end=" ")

