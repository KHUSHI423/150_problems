if __name__ == "__main__":
    s = input("Enter a string: ")
    char_count = {}
    for i  in s:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    for char, count in char_count.items():
        print(f"{char}{count}",end="")
