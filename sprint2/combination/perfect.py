if __name__ == "__main__":
    n = int(input("enter the number: "))
    if (n**0.5) == int(n**0.5):
        print("perfect square")
    else:
        print("not a perfect square")
    if (n**(1//3)) == int(n**(1//3)):
        print("perfect cube")
    else:
        print("not a perfect cube")