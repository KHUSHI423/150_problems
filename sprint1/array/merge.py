if __name__ == "__main__":
    arr1 = list(map(int, input("Enter the elements of the first array separated by spaces: ").split()))
    arr2 = list(map(int, input("Enter the elements of the second array separated by spaces: ").split()))
    merged_array = arr1 + arr2
    merged_array.sort()
    print("The merged and sorted array is:", merged_array)