if __name__ == "__main__":
    s = input("Enter a string: ")
    ans =""
    for i in s:
        if i not in ans:
            ans+=i
    print("The string after removing duplicates is:", ans)