n = int(input())
steps = 1
ans = []
while n!=1:
    ans.append(n)
    if n%2 == 0:
        n//=2
    else:
        n = n*3 + 1

for i in ans:
    print(i,end="-")
print(1)
        
