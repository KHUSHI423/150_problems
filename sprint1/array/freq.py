if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for num, count in freq.items():
        print(f"{num} : {count}")