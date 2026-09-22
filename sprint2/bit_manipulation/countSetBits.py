if __name__ == "__main__" :
    integerNumber = int(input("enter the value: "))
    countBits = 0 
    while integerNumber:
        if integerNumber & 1 :
                countBits +=1
        integerNumber >>= 1
    print(countBits)
    
        
