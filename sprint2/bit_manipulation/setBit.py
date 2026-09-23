n = int(input("Enter the integer: "))

lowestSet = (n & -n).bit_length() - 1
highestSet = n.bit_length() - 1

print("Lowest set bit:", lowestSet)
print("Highest set bit:", highestSet)