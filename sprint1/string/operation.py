if __name__ == "__main__":
    s = input("Enter a string: ")
    k = int(input("Enter the shift value: "))
    operation = int(input("Enter the operation (encode = 1/decode = 0): "))
    if operation == 1:
        encoded = ""
        for c in s:
            if c.isalpha():
                shift = k % 26
                if c.islower():
                    encoded += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
                else:
                    encoded += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
            else:
                encoded += c
        print(f"The encoded string is: {encoded}")
    elif operation == 0:
        decoded = ""
        for c in s:
            if c.isalpha():
                shift = k % 26
                if c.islower():
                    decoded += chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
                else:
                    decoded += chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
            else:
                decoded += c
        print(f"The decoded string is: {decoded}")