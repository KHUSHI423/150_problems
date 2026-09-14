
if __name__ == "__main__":
    a = input("Enter a string: ")
    b = input("Enter another string: ") 
    char_count = {}
    for char in a:
        char_count[char] = char_count.get(char, 0) + 1

    flag = 0
    for char in b:
        if char_count[char] == 0:
            print("The strings are not anagrams.")
            flag = 1
            break
        char_count[char] -= 1
    if flag == 0:
        print("The strings are anagrams.")
    