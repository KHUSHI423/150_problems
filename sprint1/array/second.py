if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    if len(arr) < 2:
        print("Array must have at least two elements.")
    else:
        second_largest = second_smallest = arr[0]
        largest = smallest = arr[0]

        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num

            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest and num != smallest:
                second_smallest = num

        print("Second largest element is:", second_largest)
        print("Second smallest element is:", second_smallest)