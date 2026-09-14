if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    ans = []
    for i in arr:
        if i < 2:
            continue
        else:
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    break
            else:
                ans.append(i)
    print("The prime numbers in the array are:", ans)
    print("sum of prime numbers in the array is:", sum(ans))