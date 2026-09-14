if __name__ == "__main__":
   arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
   print("maximum:", max(arr))
   print("minimum:", min(arr))
   print("sum:", sum(arr))
   print("average:", f"{sum(arr)/len(arr):.2f}")