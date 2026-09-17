if __name__ == "__main__" :
    n = int(input("enter the of elements: "))
    sum_of_square = 0
    sum_of_cube = 0
    alternative = 0
    for i in range(1,n+1):
        sum_of_cube+= i**3
        sum_of_square+= i**2
        if i%2 ==0:
            alternative-=i
        else:
            alternative+=i
    print("sum of square: ",sum_of_square)
    print("sum of cube: ",sum_of_cube)
    print("alternative: ",alternative)

