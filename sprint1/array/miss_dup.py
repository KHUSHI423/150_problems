if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    miss = 0
    dup = 0
    for i in range(len(arr)):
        if arr[i] != i + 1:
            miss = i + 1
            dup = arr[i]
            break
    print("The missing number in the array is:", miss)
    print("The duplicate number in the array is:", dup)
    