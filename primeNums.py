
def getPrimeNums(n):
    
    prime = list()
    num = 2
    while num <= n:
        
        flag = False
        for i in range(2, num):
            if num % i == 0:
                flag = True
                break

        if flag == False:
            prime.append(num)

        num += 1

    return prime

# Driver Code.
n = 40
print(getPrimeNums(n))
