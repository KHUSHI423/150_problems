if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    k = int(input("Enter the number of positions to rotate the array: "))
    k = k % len(arr)
    def rotate_array(arr,s,e):
        while s<e:
            arr[s],arr[e]=arr[e],arr[s]
            s+=1
            e-=1
        return arr
    arr=rotate_array(arr,0,len(arr)-1)
    arr=rotate_array(arr,0,k-1)
    arr=rotate_array(arr,k,len(arr)-1)
    print(arr)

    
    
        
    """
    def rotate_array(arr, k):
            return arr[-k:] + arr[:-k]
    print("The rotated array is:", rotate_array(arr, k))
        """