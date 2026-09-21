if __name__ == "__main__":
    n =int(input("enter value for iteration: "))
    r = []
    m = []
    for i in range(n):
        r.append(int(input(f"enter the {i+1} remainder : ")))
        m.append(int(input(f"enter the  {i+1} divisor : ")))
    i = 1
    while True:
        valid = True
        for j in range(len(r)):
            if i%m[j] != r[j]:
                valid = False
                break
        if valid :
            print("smallest positive integer: ",i)
            break
        else:
            i+=1
        
