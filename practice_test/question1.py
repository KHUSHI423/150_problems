array = list(map(int,input("enter the elements of the array: ").split()))
length_of_array = len(array)

prime_list =[]

def prime(num):
    if num == 2:
        return True
    for i in range(2,num): 
        if num % i == 0:
            return False
    return True
    


for i in range(length_of_array):
    if prime(array[i]):
        prime_list.append(array[i])

sum_of_prime = sum(prime_list)

print("the prime values are: ",prime_list)
print("sum of prime values: ",sum_of_prime)



    