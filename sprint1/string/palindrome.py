if __name__ == "__main__":
    s = input("Enter a string: ")
    l = len(s) 
    i = 0
    while i <= l-1:
        if s[i] != s[l-1-i]:
            print("The string is not a palindrome.")
            break
        i += 1
    if i == l:
        print("The string is a palindrome.")    