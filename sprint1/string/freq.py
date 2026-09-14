if __name__ == "__main__":
    s = input("Enter a string: ")
    char = {}
    for i in s:
        if i in char:
            char[i] += 1
        else:
           char[i]=1
    for i in char:
        print(f"{i} : {char[i]}")