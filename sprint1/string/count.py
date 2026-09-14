if __name__ == "__main__":
    s = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    print(f"The number of vowels in the string is: {count}")
    print(f"The number of consonants in the string is: {len(s) - count}")