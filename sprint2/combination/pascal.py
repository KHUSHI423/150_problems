if __name__ == "__main__":
  n  = int(input("Enter the number of rows: "))
  def fact(n):
    if n <= 1:
      return 1
    return n*fact(n-1)
  def comb(i,j):
    return fact(i)//(fact(j)*fact(i-j))
  for i in range(n): 
    for j in range(n-1-i):
      print(" ",end="")
    
    for j in range(2*i + 1):
        if j>=0 and j<=i:
          print(comb(i,j),end=" ")
    print()
          
   