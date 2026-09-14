if __name__ == "__main__":
    n = int(input("Enter the number: "))
    l = len(str(n))
    flag = 0
    i = 0
    while i <= l-1:
        if str(n)[i] != str(n)[l-1-i]:
            flag = 1
            break
        i += 1
    if flag == 0:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
