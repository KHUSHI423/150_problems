if __name__ == "__main__" :
    integerRep = int(input("enter the integer: "))
    ans = ""
    while integerRep :
          ans =  str(integerRep%2) + ans
          integerRep//=2
    print(ans)
    '''
    n = int(input("Enter integer: "))
print(bin(n)[2:])
'''